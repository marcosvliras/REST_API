"""Update."""
from fastapi import APIRouter, Query
from src.infra.sqlitedb import DbSqlite

router = APIRouter()


@router.put("/register", description="Updated the User Name")
def update(
    user_name: str = Query(title="USER NAME"),
    new_user_name: str = Query(title="New USER NAME"),
):
    """Update."""
    db = DbSqlite()
    db.update(user_name=user_name, new_user_name=new_user_name)
