# setup_inicial.py
import os
import sys

# Garante que o diretório raiz esteja no path para evitar erros de importação
sys.path.append(os.path.abspath("."))

from app.database.db_init import criar_tabelas
from app.database.conexao import SessionLocal
from app.models.user import User  # ✅ Import correto
from passlib.context import CryptContext

# Configura o contexto de criptografia para senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def criar_usuario_inicial():
    print("🔐 Criar usuário inicial de acesso à plataforma")
    username = input("👤 Nome de usuário: ").strip()
    password = input("🔑 Senha: ").strip()

    if not username or not password:
        print("❌ Nome de usuário e senha não podem estar vazios.")
        return

    hashed_password = pwd_context.hash(password)

    db = SessionLocal()

    # Verifica se já existe um usuário com esse nome
    usuario_existente = db.query(User).filter(User.username == username).first()
    if usuario_existente:
        print(f"⚠️ Usuário '{username}' já existe. Escolha outro nome.")
        db.close()
        return

    # Criação do usuário
    novo_usuario = User(username=username, hashed_password=hashed_password)
    db.add(novo_usuario)
    db.commit()
    db.close()
    print(f"✅ Usuário '{username}' criado com sucesso!")

if __name__ == "__main__":
    print("\n🚀 Iniciando configuração inicial da plataforma...\n")

    try:
        print("📦 Criando todas as tabelas do banco de dados...")
        criar_tabelas()
        print("✅ Tabelas criadas com sucesso.")
        criar_usuario_inicial()
    except Exception as e:
        print("❌ Erro durante o processo:", str(e))
