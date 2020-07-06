import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")  # dev, stage, prod
    testing: bool = os.getenv("TESTING", False)


@lru_cache()
def get_settings():
    log.info("Loading config settings from the environment")
    return Settings()
