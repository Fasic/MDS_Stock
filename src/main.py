from fastapi import FastAPI

from .api import router as api_router

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
)

app.include_router(api_router)
