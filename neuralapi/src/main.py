import logging
import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.imaging import imaging_router

from core.settings import settings


app = FastAPI(
    title=settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


app.include_router(
    imaging_router,
    prefix="/api/v1/authorization",
    tags=["authorization"],
)


if __name__ == "__main__":
    logging.info("start auth service")
    uvicorn.run(
        "main:app",
        host=settings.auth_host,
        port=settings.auth_port,
        log_level="debug",
        reload=True,
    )
