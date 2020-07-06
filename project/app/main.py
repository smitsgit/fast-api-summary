from fastapi import FastAPI

app = FastAPI()


@app.get('/ping')
def hello():
    return {'ping': 'pong'}
