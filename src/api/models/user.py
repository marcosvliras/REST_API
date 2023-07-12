"""User."""
from pydantic import BaseModel, Field


class User(BaseModel):
    """User Model."""

    user_name: str = Field(title="Username")
    symbol: str = Field(
        title="Symbol of a cripto supported by MercadoBitcoin's API"
    )
