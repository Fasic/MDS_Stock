from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from pydantic import constr

from src.services.stock_service import StockService

router = APIRouter(prefix="/analytics", tags=["analytics"])

date_format_regex = r"^\d{4}-\d{2}-\d{2}$"


@router.get("/stock", response_model=None)
async def get_stock_data(
    company: str,
    from_date: constr(pattern=date_format_regex) = Query(None, alias="from", description="Date in format YYYY-MM-DD"),
    to_date: constr(pattern=date_format_regex) = Query(None, alias="to", description="Date in format YYYY-MM-DD"),
    service: StockService = Depends(),
):
    try:
        from_date_parsed = datetime.strptime(from_date, "%Y-%m-%d").date()
        to_date_parsed = datetime.strptime(to_date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    return await service.get_stock_analytics(company, from_date_parsed, to_date_parsed)
