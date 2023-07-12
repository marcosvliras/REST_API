"""Register."""
from fastapi import APIRouter
import logging
from src.infra import Consumer
from src.api.models import User
from src.infra.sqlitedb import DbSqlite
import yaml
from datetime import datetime
from src.api.models import RegisterResponse


router = APIRouter()


@router.post(
    "/register",
    description="register your user on the database",
    response_model=RegisterResponse,
)
def register(user: User):
    """Register."""
    with open("./src/infra/coins.yml", "r") as file:
        try:
            coins = yaml.load(file, Loader=yaml.loader.SafeLoader)
        except yaml.YAMLError as exc:
            logging.error(exc)
            raise exc

    consumer = Consumer()
    response = consumer.get(user.symbol)
    coin = coins[f"{user.symbol}"]
    high = response["ticker"]["buy"]
    low = response["ticker"]["sell"]
    date = response["ticker"]["date"]
    date = datetime.utcfromtimestamp(date).strftime("%d/%m/%Y")

    db = DbSqlite()
    db.create_table()
    user_id = db.get_user_id(user.user_name)
    db.insert_values(
        user_id, user.user_name, coin, user.symbol, low, high, date
    )

    r = RegisterResponse(
        user_id=user_id,
        user_name=user.user_name,
        coin=coin,
        symbol=user.symbol,
        buy=high,
        sell=low,
        date=date,
    )
    return r
