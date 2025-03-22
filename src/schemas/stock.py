from datetime import date
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
