# No seu arquivo db.py ou em algum lugar onde você inicializa o SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Assumindo que você já tem essas definições
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" # Ou o caminho do seu banco de dados

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # Você provavelmente já tem isso definido em algum lugar

# Importe seus modelos aqui para que o Base saiba sobre eles
# from app.models.alerta import Alerta # Se Alerta for definida em alerta.py e herdando de Base

def create_db_tables():
    # Isso cria todas as tabelas que herdam de Base
    # Certifique-se de que seus modelos (como Alerta) estão importados
    # antes de chamar create_all() para que o SQLAlchemy os reconheça.
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

# Chame esta função na inicialização da sua aplicação
# Por exemplo, no seu main.py, antes de iniciar o Uvicorn, ou em um script separado.
# Exemplo simples para main.py:
# from app.database.db import create_db_tables
# create_db_tables()