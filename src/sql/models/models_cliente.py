# BIBLIOTECA 
from sqlalchemy import Column, String, Integer
from src.config.database import Base


#CRIANDO MODELS 

class ModelsCliente(Base):
    __tablename__ = 'cliente'
    id = Column(String, primary_key=True,index=True)
    nome = Column(String)
    moedas = Column(Integer)
    