from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VESION)


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}
