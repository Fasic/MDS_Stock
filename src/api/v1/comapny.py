from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from peewee import DoesNotExist

from src.schemas.company import CompanyCreate
from src.schemas.company import CompanyResponse
from src.schemas.company import CompanyUpdate
from src.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["companies"])


@router.post("/", response_model=CompanyResponse)
async def create_company(company: CompanyCreate, service: CompanyService = Depends()):
    return await service.create_company(company)


@router.get("/", response_model=List[CompanyResponse])
async def read_companies(page: int = 1, items_per_page: int = 10, service: CompanyService = Depends()):
    return await service.get_all_companies(page, items_per_page)


@router.get("/{company_id}", response_model=CompanyResponse)
async def read_company(company_id: int, service: CompanyService = Depends()):
    try:
        return await service.get_company(company_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Company not found")


@router.put("/{company_id}", response_model=CompanyResponse)
async def update_company(company_id: int, company: CompanyUpdate, service: CompanyService = Depends()):
    try:
        return await service.update_company(company_id, company)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Company not found")


@router.delete("/{company_id}", response_model=bool)
async def delete_company(company_id: int, service: CompanyService = Depends()):
    try:
        return await service.delete_company(company_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Company not found")
