"""Get coin."""
from fastapi import APIRouter
from src.infra import Consumer
from src.api.models import GetResponse
from datetime import datetime

router = APIRouter()


@router.get(
    "/get", description="Get info about the coin", response_model=GetResponse
)
def get(coin: str):
    """Get coin."""
    consumer = Consumer()
    response = consumer.get(coin)

    date = response["ticker"]["date"]
    date = datetime.utcfromtimestamp(date).strftime("%d/%m/%Y")
    r = GetResponse(
        buy=response["ticker"]["buy"],
        sell=response["ticker"]["sell"],
        date=date,
    )
    return r
