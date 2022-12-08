import os

from pydantic import BaseSettings


class Config(BaseSettings):
    API_V1_PREFIX = "/v1"


config = Config()
