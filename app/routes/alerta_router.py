# app/routes/alerta_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.conexao import SessionLocal
from app.models.alerta import Alerta
from app.schemas.alerta_schema import AlertaSchema
from typing import List
from app.utils.security import get_current_user
from app.models.user import User

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


#@router.get("/protegida")
#def rota_segura(usuario: User = Depends(get_current_user)):
    #return {"msg": f"Olá,{usuario.username}. Você está #autenticado!"}
