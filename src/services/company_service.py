from typing import List

from peewee import DoesNotExist

from src.models.company import Company
from src.schemas.company import CompanyCreate
from src.schemas.company import CompanyResponse
from src.schemas.company import CompanyUpdate


class CompanyService:
    @staticmethod
    async def create_company(company_data: CompanyCreate) -> CompanyResponse:
        company = Company.create(**company_data.model_dump())
        return CompanyResponse.model_validate(company.__data__)

    @staticmethod
    async def get_company(company_id: int) -> CompanyResponse:
        try:
            company = Company.get_by_id(company_id)
            return CompanyResponse.model_validate(company.__data__)
        except DoesNotExist:
            raise DoesNotExist("Company not found")

    @staticmethod
    async def get_all_companies(page: int, items_per_page: int) -> List[CompanyResponse]:
        companies = list(Company.select().paginate(page, items_per_page))
        return [CompanyResponse.model_validate(company.__data__) for company in companies]

    @staticmethod
    async def update_company(company_id: int, company_data: CompanyUpdate) -> CompanyResponse:
        try:
            Company.update(company_data.model_dump(exclude_none=True)).where(Company.id == company_id).execute()
            company = Company.get_by_id(company_id)
            return CompanyResponse.model_validate(company.__data__)
        except DoesNotExist:
            raise DoesNotExist("Company not found")

    @staticmethod
    async def delete_company(company_id: int) -> bool:
        try:
            Company.delete().where(Company.id == company_id).execute()
            return True
        except DoesNotExist:
            raise DoesNotExist("Company not found")
