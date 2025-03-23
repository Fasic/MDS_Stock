from datetime import date
from typing import List
from typing import Optional

from pydantic import BaseModel


class StockCreate(BaseModel):
    company: int
    date: date
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: int


class StockUpdate(BaseModel):
    company_id: Optional[int] = None
    date: Optional[date] = None
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    adj_close: Optional[float] = None
    volume: Optional[int] = None


class StockResponse(BaseModel):
    id: int
    company: str
    date: date
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: int

    class Config:
        orm_mode: True
        model_validate: True


class StockData(BaseModel):
    date: date
    close: float

    class Config:
        orm_mode: True
        model_validate: True


class StockMaxProfitData(BaseModel):
    buy: Optional[StockData]
    sell: Optional[StockData]
    profit: float


class StockDataResponse(StockMaxProfitData):
    max_profit: Optional[float]
    better_buy: Optional[List[str]]
    from_to: str


class StockAnalytics(StockDataResponse):
    future_period: StockDataResponse
    past_period: StockDataResponse
