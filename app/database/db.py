# app/database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# **Ajuste o caminho do banco de dados para coincidir com o nome do seu arquivo.**
# Se você quer que o arquivo seja "alertas.db" na raiz do projeto:
SQLALCHEMY_DATABASE_URL = "sqlite:///./alertas.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} # Necessário para SQLite em FastAPI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# A função get_db para as dependências do FastAPI (você já deve ter isso)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()