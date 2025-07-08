# app/schemas/alerta_schema.py

from pydantic import BaseModel

class AlertaSchema(BaseModel):
    id: int
    time_1: str
    time_2: str
    mercado: str
    odd: str

    class Config:
        from_mode = True  # permite converter de SQLAlchemy para Pydantic
