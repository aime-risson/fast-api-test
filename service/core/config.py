from starlette.datastructures import CommaSeparatedStrings
import os
from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseSettings


class Settings(BaseSettings):
    aws_default_region: str
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()

ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
API_V1_STR = "/api/v1"
PROJECT_NAME = "Search Market Place "
