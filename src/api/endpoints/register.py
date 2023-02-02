from fastapi import APIRouter, Query
from src.infra import Consumer
from src.api.models import User
from src.infra.sqlitedb import DbSqlite
import yaml
from datetime import datetime
from src.api.models import RegisterResponse
from typing import Optional


router = APIRouter()

@router.post('/register', description='register your user on the database',
    response_model=RegisterResponse)
def register(user: User):
    
    with open('./src/infra/coins.yml', 'r') as file:
        try:
            coins = yaml.load(file, Loader=yaml.loader.SafeLoader)
        except yaml.YAMLError as exc:
            print(exc)

    consumer = Consumer() 
    response = consumer.get(user.symbol)
    coin = coins[f"{user.symbol}"]
    high = response['ticker']['buy'] 
    low = response['ticker']['sell']
    date = response['ticker']['date']
    date = datetime.utcfromtimestamp(date).strftime('%d/%m/%Y')

    db = DbSqlite()
    db.create_table()
    user_id = db.get_user_id(user.user_name)
    db.insert_values(user_id, user.user_name, coin, user.symbol, low, high, date)

    r = RegisterResponse(
        user_id=user_id,
        user_name=user.user_name,
        coin=coin,
        symbol=user.symbol,
        buy=high,
        sell=low,
        date=date
    )
    return r


@router.delete('/register', description='Delete user')
def delete(
    user_name: str = Query(title='USER NAME'),
    symbol: Optional[str] = Query(None, title='Symbol of a cripto')
):
    db = DbSqlite()
    db.delete(user_name=user_name, symbol=symbol)


@router.put('/register', description='Updated the User Name')
def update(
    user_name: str = Query(title='USER NAME'),
    new_user_name: str = Query(title='New USER NAME')
):
    db = DbSqlite()
    db.update(user_name=user_name, new_user_name=new_user_name)
