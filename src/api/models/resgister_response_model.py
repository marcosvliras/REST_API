from pydantic import BaseModel, Field

class RegisterResponse(BaseModel):
    user_id: int = Field(title='UserID')
    user_name: str = Field(title='User Name')
    coin: str = Field(title='Cripto')
    symbol: str = Field(title='Cripto symbol')
    buy: float = Field(title='Maior preço de oferta de compra das últimas 24 horas')
    sell: float = Field(title='Menor preço de oferta de venda das últimas 24 horas')
    date: str = Field(title='Data e hora da informação')