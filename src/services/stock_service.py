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
        return StockResponse.model_validate(stock)

    @staticmethod
    async def get_all_stocks() -> List[StockResponse]:
        stocks = Stock.select()
        return [StockResponse.model_validate(stock) for stock in stocks]

    @staticmethod
    async def get_stock(stock_id: int) -> StockResponse:
        try:
            stock = Stock.get_by_id(stock_id)
            return StockResponse.model_validate(stock)
        except DoesNotExist:
            raise DoesNotExist("Stock not found")

    @staticmethod
    async def update_stock(stock_id: int, stock_data: StockUpdate) -> StockResponse:
        try:
            Stock.update(**stock_data.model_dump()).where(Stock.id == stock_id).execute()
            stock = Stock.get_by_id(stock_id)
            return StockResponse.model_validate(stock)
        except DoesNotExist:
            raise DoesNotExist("Stock not found")

    @staticmethod
    async def delete_stock(stock_id: int) -> StockResponse:
        try:
            stock = Stock.get_by_id(stock_id)
            stock_response = StockResponse.model_validate(stock)
            stock.delete_instance()
            return stock_response
        except DoesNotExist:
            raise DoesNotExist("Stock not found")
