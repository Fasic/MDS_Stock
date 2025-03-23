from fastapi import APIRouter

from .comapny import router as company_router
from .stock_analytics import router as stock_analytics_router
from .stocks import router as stocks_router

router = APIRouter(prefix="/v1")
router.include_router(company_router)
router.include_router(stocks_router)
router.include_router(stock_analytics_router)
