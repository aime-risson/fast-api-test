from fastapi import FastAPI, Depends
from .core.config import settings
from functools import lru_cache
from fastapi.middleware.cors import CORSMiddleware

from service.api.api_v1.api import router as api_router
from service.core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod"
)

origins = ["http://localhost:3000", "https://www.vinted.fr", "https://www.carhartt-wip.com", "https://www.ralphlauren.fr", "*", "https://www.yager.eu", "https://yager.eu", "www.yager.eu", "yager.eu", ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix=API_V1_STR)


@app.get("/ping", summary="Check that the service is operational")
def pong():
    """
    Sanity check - this will let the user know that the service is operational.

    It is also used as part of the HEALTHCHECK. Docker uses curl to check that the API service is still running, by exercising this endpoint.

    """
    return {"ping": settings.aws_default_region}
