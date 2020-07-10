import os
import logging
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from app.config import Settings, get_settings
from app.api import ping, summaries
from app.database import init_db

log = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(ping.router)
    app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    return app


app = create_app()


@app.on_event("startup")
async def startup_event():
    log.info("Application starting up")
    init_db(app, os.environ.get("DATABASE_URL"))


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down")
