"""Delete."""
from fastapi import APIRouter, Query
from src.infra.sqlitedb import DbSqlite
from typing import Optional

router = APIRouter()


@router.delete("/register", description="Delete user")
def delete(
    user_name: str = Query(title="USER NAME"),
    symbol: Optional[str] = Query(None, title="Symbol of a cripto"),
):
    """Delete."""
    db = DbSqlite()
    db.delete(user_name=user_name, symbol=symbol)
