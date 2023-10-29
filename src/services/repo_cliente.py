#BIBLIOTECAS 
from sqlalchemy import *
from sqlalchemy.orm import Session
from src.sql.models.models_cliente import ModelsCliente
from src.sql.schema.schema_cliente import SchemaCliente, SchemaMoedas

# CRIAÇÃO DE REPOSITORIOS DE CLIENTES 

class repositorio_cliente():
    def __init__(self, session:Session):    
        self.session = session 

    def criar(self, cliente:SchemaCliente): 
        db_cliente = ModelsCliente(
            id = cliente.id,
            nome = cliente.nome,
            moedas = cliente.moedas
        )
        self.session.add(db_cliente)
        self.session.commit()
        self.session.refresh(db_cliente)
        return db_cliente

    def listar(self):
        stmt = select(ModelsCliente)
        cliente = self.session.execute(stmt).scalars().all()
        return cliente    


    def coin(self, moedas: SchemaMoedas):
        stmt = (
            update(ModelsCliente)
            .where(ModelsCliente.nome == moedas.nome)
            .values(moedas=moedas.moedas)
        )
        self.session.execute(stmt)
        self.session.commit()
        return stmt