from fastapi import FastAPI
from .api import router
from logging import StreamHandler, INFO
import logging
import uvicorn

logging.basicConfig(
    level=INFO,
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[StreamHandler()]
)

app = FastAPI(title='Cripto API', version="1.0.0")
app.include_router(router, prefix='/v1')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
