#BIBLIOTECAS IMPORTADAS 
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

#BIBLIOTECAS DE SISTEMA
from src.sql.schema.schema_cliente import SchemaCliente, SchemaMoedas
from src.config.database import get_db
from src.services.repo_cliente import repositorio_cliente


# CRIANDO ROTAS 

router = APIRouter()

@router.get('/home')
def home():
    return {'Deu Certo'}

@router.post('/cliente')
def criar_cliente(cliente:SchemaCliente, session:Session = Depends(get_db)):
    cliente_criado = repositorio_cliente(session).criar(cliente)
    return cliente_criado

@router.get('/cliente')
def listar(session:Session = Depends(get_db)):
    clientes = repositorio_cliente(session).listar()
    return clientes


@router.put('/cliente')
def coinEditar(moedas:SchemaMoedas, session:Session = Depends(get_db)):
    repositorio_cliente(session).coin(moedas)
    