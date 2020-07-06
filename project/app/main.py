from fastapi import FastAPI, Depends

from .config import get_settings, Settings

app = FastAPI()


@app.get('/ping')
async def hello(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong',
        'environment': settings.environment,
        'tesing': settings.testing,
    }
