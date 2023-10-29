#BLIBIOTECAS - PADRÃO 
from fastapi import FastAPI, Depends
from src.routes import rota_cliente
from src.config.database import criar_db


criar_db()
app = FastAPI()


# COLOCANDO AS ROTAS 
app.include_router(rota_cliente.router)
