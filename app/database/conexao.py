# app/database/conexao.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Caminho absoluto para o banco SQLite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, '../../alertas.db')}"

# Cria o engine (motor de conexão)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria a sessão local para ser usada nas operações com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa que será herdada pelos modelos
Base = declarative_base()
