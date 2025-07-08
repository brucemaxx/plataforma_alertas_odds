# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho do banco SQLite (você pode personalizar esse nome se quiser)
DATABASE_URL = "sqlite:///alertas.db"

# Criação da engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criação da fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base usada para os modelos
Base = declarative_base()
