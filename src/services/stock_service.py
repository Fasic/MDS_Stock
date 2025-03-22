from typing import List

from peewee import DoesNotExist

from src.models.stocks import Stock
from src.schemas.stock import StockCreate
from src.schemas.stock import StockResponse
from src.schemas.stock import StockUpdate


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
