# app/models/alerta.py
from sqlalchemy import Column, Integer, String, DateTime
from app.database.db import Base # Importando Base do db.py

class Alerta(Base):
    __tablename__ = "alertas" # O nome da tabela no banco de dados DEVE ser 'alertas'
    id = Column(Integer, primary_key=True, index=True)
    time_1 = Column(String)
    time_2 = Column(String)
    mercado = Column(String)
    odd = Column(String)
    data_envio = Column(DateTime)

    def __repr__(self):
        return f"<Alerta(id={self.id}, mercado='{self.mercado}', odd='{self.odd}')>"