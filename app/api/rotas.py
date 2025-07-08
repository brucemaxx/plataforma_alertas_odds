# app/api/rotas.py

from fastapi import APIRouter, Query
from app.scraper.bet365 import coletar_dados_validos_jogo
from app.schemas.jogo import JogoSchema
from typing import Union
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.conexao import SessionLocal
from app.models.alerta import Alerta as AlertaModel
from app.schemas.alerta import AlertaCreate, AlertaResponse


# Dependência para injetar a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()

@router.get("/jogos/validos", response_model=Union[JogoSchema, dict])
@router.post("/alerta", response_model=AlertaResponse)

def criar_alerta(alerta: AlertaCreate, db: Session = Depends(get_db)):
    """
    Cria e armazena um novo alerta no banco de dados.
    """
    novo_alerta = AlertaModel(**alerta.dict())
    db.add(novo_alerta)
    db.commit()
    db.refresh(novo_alerta)
    return novo_alerta


def get_jogo_valido(min_odd: float = Query(0.0, description="Odd mínima para filtrar")):
    """
    Rota que retorna o primeiro jogo valido capturado pela Bet365.
    """
    
    dados = coletar_dados_validos_jogo()
    if not dados:
        return {"mensagem": "Nenhum jogo válido encontrado."}
    
    try:
        odd_valor = float(dados["odd"].replace(",", ".")) # Trata odds com vírgula
    except:
        return {"mensagem": "Formato de odd inválido."}    
    
    if odd_valor >= min_odd:
        return dados
    
    else: {
        "mensagem": f"A odd ({odd_valor}) esta abaixo do limite definido ({min_odd})."
    }
    
@router.get("/alertas", response_model=list[AlertaResponse])
def listar_alertas(db: Session = Depends(get_db)):
    """
    Lista todos os alertas armazenados no banco de dados.
    """
    alertas = db.query(AlertaModel).all()
    return alertas

    