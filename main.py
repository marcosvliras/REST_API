"""Main."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import router
from logging import StreamHandler, INFO
import logging
import uvicorn

logging.basicConfig(
    level=INFO,
    format="%(levelname)s:%(asctime)s:%(message)s",
    handlers=[StreamHandler()],
)

origins = ["http://localhost:5500"]

app = FastAPI(title="Cripto API", version="1.0.0")
app.include_router(router, prefix="/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)