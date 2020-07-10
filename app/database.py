import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise, run_async

from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger(__name__)


def init_db(app: FastAPI, db_url: str):
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema():
    log.info("Initializing tortoise")
    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"), modules={"models": ["models.tortoise"]}
    )
    log.info("Generating databse schema via tortoise")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


def main():
    run_async(generate_schema())


if __name__ == "__main__":
    main()
