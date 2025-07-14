# app/main.py
from fastapi import FastAPI
from app.routes import dashboard_router
# from app.database.db import create_db_tables # REMOVA ou COMENTE esta linha!

app = FastAPI()

# Inclua seus roteadores
app.include_router(dashboard_router.router)

# NENHUMA CHAMADA PARA initialize_database() OU create_db_tables() AQUI!
# A criação do DB é feita APENAS pelo script init_db.py que você rodou manualmente.

# Exemplo de uma rota raiz (opcional)
@app.get("/")
def read_root():
    return {f"Bem-vindo à Plataforma de Alertas de Odds!"}