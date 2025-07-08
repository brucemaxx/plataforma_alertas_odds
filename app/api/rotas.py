# app/api/rotas.py

from fastapi import APIRouter, Query
from app.scraper.bet365 import coletar_dados_validos_jogo
from app.schemas.jogo import JogoSchema
from typing import Union

router = APIRouter()

@router.get("/jogos/validos", response_model=Union[JogoSchema, dict])

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