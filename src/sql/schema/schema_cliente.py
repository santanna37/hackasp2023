# BIBLIOTECAS 
from pydantic import BaseModel
from typing import Optional


# SCHEMA DE CLIENTE

class SchemaCliente(BaseModel):
    id: str
    nome: str
    moedas: Optional[int] = 0

    class Config: 
        orm_mode = True

class SchemaMoedas(BaseModel):
    nome: str
    moedas: int

    class Config: 
        orm_mode = True
