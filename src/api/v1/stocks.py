from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from peewee import DoesNotExist

from src.schemas.stock import StockCreate
from src.schemas.stock import StockResponse
from src.schemas.stock import StockUpdate
from src.services.stock_service import StockService

router = APIRouter(prefix="/stocks", tags=["stocks"])


@router.post("/", response_model=StockResponse)
async def create_stock(stock: StockCreate, service: StockService = Depends()):
    return await service.create_stock(stock)


@router.get("/", response_model=List[StockResponse])
async def read_stocks(service: StockService = Depends()):
    return await service.get_all_stocks()


@router.get("/{stock_id}", response_model=StockResponse)
async def read_stock(stock_id: int, service: StockService = Depends()):
    try:
        return await service.get_stock(stock_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Stock not found")


@router.put("/{stock_id}", response_model=StockResponse)
async def update_stock(stock_id: int, stock: StockUpdate, service: StockService = Depends()):
    try:
        return await service.update_stock(stock_id, stock)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Stock not found")


@router.delete("/{stock_id}", response_model=StockResponse)
async def delete_stock(stock_id: int, service: StockService = Depends()):
    try:
        return await service.delete_stock(stock_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Stock not found")
