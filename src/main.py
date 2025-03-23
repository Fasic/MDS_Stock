from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api import router as api_router
from .setup.logger import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield


app = FastAPI(
    docs_url="/docs",
    openapi_url="/v1/openapi.json",
    title="Stock api app",
    description="Interview app for MDS Informaticki Inzenjering.",
    version="1.0.0",
    terms_of_service="",
    contact={
        "name": "Filip Vasic",
        "email": "wasicfilip93@gmail.com",
    },
    lifespan=lifespan,
)

app.include_router(api_router)
