from typing import Optional
from fastapi import APIRouter, Query
from src.infra.sqlitedb import DbSqlite

router = APIRouter()

@router.get('/fetch', description='Get info from the database.')
def fetch(
    user_name: Optional[str] = Query(None, title='User Name'),
    user_id: Optional[str] = Query(None, title='User ID'),
    all: Optional[bool] = Query(True, title='Get all database')
):
    db = DbSqlite()
    r = db.select(
        user_name=user_name, user_id=user_id, all=all)
    return r
