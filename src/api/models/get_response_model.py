from pydantic import BaseModel, Field

class GetResponse(BaseModel):
    buy: float = Field(title='Maior preço de oferta de compra das últimas 24 horas')
    sell: float = Field(title='Menor preço de oferta de venda das últimas 24 horas')
    date: str = Field(title='Data e hora da informação')