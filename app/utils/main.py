# main.py

from fastapi import FastAPI
from app.api.rotas import router
from app.routes import alerta_router

app = FastAPI(
    title="Plataforma de Odds",
    description="API para análise e alerta de odds da Bet365",
    version="1.0.0"
)

app.include_router(alerta_router.router) # Adiciona o router de alertas

@app.get("/")
def raiz():
    return {"mensagem": "API de Alertas de Odds no ar!"}
