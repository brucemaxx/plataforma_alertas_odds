# app/models/alerta.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

# Declarative base (a maioria das apps usa a mesma base importada de um lugar central)
Base = declarative_base()

class Alerta(Base):
    """
    Modelo da tabela de alertas disparados. Cada entrada representa um alerta enviado.
    """
    __tablename__ = "alertas" # => Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True) # => ID autoincrementável
    time_1 = Column(String, nullable=False) # => Nome do primeiro time
    time_2 = Column(String, nullable=False) # => Nome do segundo time
    mercado = Column(String, nullable=False) # => Nome do mercado (ex: Mais de, Resultado  Final)
    odd = Column(Float, nullable=False) # => Valor da odd
    data_envio = Column(DateTime, default=datetime.utcnow) # => Data/hora que foi enviado
    
    def __repr__(self):
        return f"<Alerta {self.time_1} x {self.time_2} | {self.mercado} - {self.odd}>"
