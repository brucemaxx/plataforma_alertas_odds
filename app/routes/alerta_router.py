# app/routes/alerta_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.conexao import SessionLocal
from app.models.alerta import Alerta
from app.schemas.alerta_schema import AlertaSchema
from typing import List

# Retorna todos os alertas em formato JSON
router = APIRouter()

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/alertas", response_model=List[AlertaSchema])
def listar_alertas(db: Session = Depends(get_db)):
    alertas = db.query(Alerta).all()
    return alertas
