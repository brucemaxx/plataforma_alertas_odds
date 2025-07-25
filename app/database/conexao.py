# app/database/conexao.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./alertas.db"  # ou PostgreSQL/MySQL conforme seu caso

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # se for SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ✅ Função que precisa estar presente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
