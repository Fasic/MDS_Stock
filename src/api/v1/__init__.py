from fastapi import APIRouter

from .stocks import router as stocks_router
from .test import router as test_router

router = APIRouter(prefix="/v1")
router.include_router(test_router)
router.include_router(stocks_router)
