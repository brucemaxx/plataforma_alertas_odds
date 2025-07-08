# ✅ db_init.py
# Responsável por criar as tabelas no banco de dados com base nos modelos declarados
# Este script deve ser executado uma única vez para inicializar o banco.

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Força o script a executar, motivo ele não estava sendo lido.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importe o modelo corretamente de acordo com a estrutura atual do projeto
from app.models.alerta import Alerta 
from app.database.base import Base  # Base declarativa

# Caminho para o banco SQLite
DATABASE_URL = "sqlite:///alertas.db"

# Criar engine
engine = create_engine(DATABASE_URL)

# Criar as tabelas definidas nos modelos importados (como Alerta)
print("🔧 Criando tabelas no banco de dados...")
Base.metadata.create_all(engine)
print("✅ Tabelas criadas com sucesso!")
