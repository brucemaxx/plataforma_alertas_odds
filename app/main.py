# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import alerta_router, dashboard_router
from fastapi.staticfiles import StaticFiles




app = FastAPI(
    title="Plataforma de Odds",
    description="API para análise e alerta de odds da Bet365",
    version="1.0.0"
)

# Configuração do CORS (caso queira usar frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos HTTP
)



# Adiciona o router do dashboard
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(dashboard_router.router, tags=["dashboard"])  # Adiciona o router do dashboard
app.include_router(alerta_router.router, prefix="/alertas", tags=["Alertas"]) # Adiciona o router de alertas

@app.get("/")
def raiz():
    return {"mensagem": "API de Alertas de Odds no ar!"}
