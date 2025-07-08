# main.py

from fastapi import FastAPI
from app.api.rotas import router

app = FastAPI(
    title="Plataforma de Odds",
    description="API para análise e alerta de odds da Bet365",
    version="1.0.0"
)

app.include_router(router)
