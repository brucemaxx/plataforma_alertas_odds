# app/schemas/alerta.py

from pydantic import BaseModel
from typing import Optional

# 🔹 Este modelo define os campos que o usuário deve enviar para criar um novo alerta
class AlertaCreate(BaseModel):
    time_1: str          # Nome do primeiro time
    time_2: str          # Nome do segundo time
    mercado: str         # Nome do mercado (ex: "resultado final", "mais de 2.5", etc)
    odd: float           # Valor da odd (cotação) a ser alertada

    class Config:
        schema_extra = {
            "example": {
                "time_1": "Flamengo",
                "time_2": "Palmeiras",
                "mercado": "resultado final",
                "odd": 3.25
            }
        }


# 🔹 Este modelo define os campos retornados pela API após salvar um alerta
class AlertaResponse(AlertaCreate):
    id: int              # ID gerado automaticamente pelo banco

    class Config:
        orm_mode = True  # Importante para integração com SQLAlchemy (permite conversão ORM → Pydantic)
