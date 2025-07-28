# app/database/db_init.py

from app.database.conexao import engine, Base
from app.models.user import User  # Garante que a tabela 'users' seja criada

def criar_tabelas():
    print("📦 Criando todas as tabelas do banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas criadas com sucesso.")

if __name__ == "__main__":
    criar_tabelas()
