import os
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from app.config import Settings, get_settings
from app.api import ping


def create_app(db_url) -> FastAPI:
    app = FastAPI()
    register_tortoise(app,
                      db_url=db_url,
                      modules={"models": ["app.models.tortoise"]},
                      generate_schemas=True,
                      add_exception_handlers=True
                      )
    app.include_router(ping.router)
    return app


app = create_app(os.environ.get("DATABASE_URL"))
