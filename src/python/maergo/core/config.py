import os

from enum import Enum

from pydantic import BaseSettings


class Env(Enum):
    DEV = "dev"
    STAGE = "stg"
    PROD = "prod"


class Config(BaseSettings):
    ENV = os.getenv("ENV", "dev")
    PORT = int(os.getenv("PORT", "8000"))
    API_V1_PREFIX = "/v1"
    POSTGRES_CONNECTION_URL = os.getenv("POSTGRES_CONNECTION_URL", "mongodb://mongodb/")


config = Config()
