# app/schemas/alerta.py

from pydantic import BaseModel
from typing import Optional

# 🔹 Este modelo define os campos que o usuário deve enviar para criar um novo alerta
class AlertaBase(BaseModel):
    time_1: str          # Nome do primeiro time
    time_2: str          # Nome do segundo time
    mercado: str         # Nome do mercado (ex: "resultado final", "mais de 2.5", etc)
    odd: float           # Valor da odd (cotação) a ser alertada

    class Config:
        from_attributes = True
        
class AlertaCreate(AlertaBase):
    """Schema usado ao criar um novo alerta (sem ID ainda)."""
    pass


class AlertaResponse(AlertaBase):
    """Schema usado para retornar um alerta com ID"""
    id: int
            


    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
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
        from_mode = True  # Importante para integração com SQLAlchemy (permite conversão ORM → Pydantic)
