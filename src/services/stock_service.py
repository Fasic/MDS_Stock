from datetime import date
from typing import List

from peewee import DoesNotExist

from src.models import Company
from src.models.stocks import Stock
from src.schemas.stock import StockAnalytics
from src.schemas.stock import StockCreate
from src.schemas.stock import StockData
from src.schemas.stock import StockDataResponse
from src.schemas.stock import StockResponse
from src.schemas.stock import StockUpdate
from src.utilities.stock_utils import stock_max_profit
from src.utilities.stock_utils import stock_one_time_max_profit


class StockService:
    @staticmethod
    async def create_stock(stock_data: StockCreate) -> StockResponse:
        stock = Stock.create(**stock_data.model_dump())
        return StockResponse.model_validate({**stock.__data__, "company": stock.company.name})

    @staticmethod
    async def get_all_stocks(company_id: int, page: int, items_per_page: int) -> List[StockResponse]:
        if company_id:
            stocks = list(Stock.select().where(Stock.company == company_id).paginate(page, items_per_page))
        else:
            stocks = list(Stock.select().paginate(page, items_per_page))
        return [StockResponse.model_validate({**stock.__data__, "company": stock.company.name}) for stock in stocks]

    @staticmethod
    async def get_stock(stock_id: int) -> StockResponse:
        try:
            stock = Stock.get_by_id(stock_id)
            return StockResponse.model_validate({**stock.__data__, "company": stock.company.name})
        except DoesNotExist:
            raise DoesNotExist("Stock not found")

    @staticmethod
    async def update_stock(stock_id: int, stock_data: StockUpdate) -> StockResponse:
        try:
            Stock.update(**stock_data.model_dump(exclude_none=True)).where(Stock.id == stock_id).execute()
            stock = Stock.get_by_id(stock_id)
            return StockResponse.model_validate({**stock.__data__, "company": stock.company.name})
        except DoesNotExist:
            raise DoesNotExist("Stock not found")

    @staticmethod
    async def delete_stock(stock_id: int) -> bool:
        try:
            Stock.delete().where(Stock.id == stock_id).execute()
            return True
        except DoesNotExist:
            raise DoesNotExist("Stock not found")

    async def get_stock_analytics(self, short_name: str, from_date: date, to_date: date) -> StockAnalytics:
        other = self.__get_other_companies(short_name)

        date_diff = to_date - from_date
        future_date = to_date + date_diff
        past_date = from_date - date_diff

        profit_data_response: StockDataResponse = self.__get_company_profit_data(short_name, from_date, to_date, other)
        future_profit_data_response: StockDataResponse = self.__get_company_profit_data(short_name, to_date, future_date, other)
        past_profit_data_response: StockDataResponse = self.__get_company_profit_data(short_name, past_date, from_date, other)

        return StockAnalytics(**profit_data_response.model_dump(), future_period=future_profit_data_response, past_period=past_profit_data_response)

    @staticmethod
    def __get_other_companies(short_name: str):
        return [company.short_name for company in list(Company.select(Company.short_name).where(Company.short_name != short_name))]

    def __get_company_profit_data(self, short_name: str, from_date: date, to_date: date, other_companies: List[str]) -> StockDataResponse:
        stocks_data = self.__get_stocks_for_company_in_period(short_name, from_date, to_date)
        one_time_max_profit = stock_one_time_max_profit(stocks_data)
        max_profit = stock_max_profit(stocks_data)
        better_buy = self.__get_better_other_companies(max_profit, from_date, to_date, other_companies)
        return StockDataResponse(**one_time_max_profit.model_dump(), max_profit=max_profit, from_to=f"{from_date}-{to_date}", better_buy=better_buy)

    def __get_better_other_companies(self, max_profit: float, from_date: date, to_date: date, other_companies: List[str]):
        better_companies = []
        for company in other_companies:
            stocks_data = self.__get_stocks_for_company_in_period(company, from_date, to_date)
            other_max_profit = stock_max_profit(stocks_data)
            if other_max_profit > max_profit:
                better_companies.append(company)
        return better_companies

    @staticmethod
    def __get_stocks_for_company_in_period(short_name: str, from_date: date, to_date: date) -> List[StockData]:
        stocks = list(
            Stock.select(Stock.date, Stock.close, Stock.volume)
            .join(Company)
            .where((Company.short_name == short_name) & (Stock.date >= from_date) & (Stock.date <= to_date))
            .order_by(Stock.date)
        )
        return [StockData.model_validate({**stock.__data__}) for stock in stocks if stock.volume > 0]
