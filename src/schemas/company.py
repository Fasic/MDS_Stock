from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str
    short_name: str
    added_to_stock_market: Optional[datetime] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    name: Optional[str] = None
    short_name: Optional[str] = None
    added_to_stock_market: Optional[datetime] = None


class CompanyResponse(CompanyBase):
    id: int
    name: str
    short_name: str
    added_to_stock_market: datetime

    class Config:
        orm_mode: True
        model_validate: True
