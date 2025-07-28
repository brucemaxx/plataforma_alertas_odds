# criar_usuario.py

import os
import sys
from passlib.context import CryptContext
from sqlalchemy.orm import Session

# Ajusta caminho do app/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

# Importações do projeto
from app.database.conexao import engine
from app.models.user import User  # Classe do modelo
from sqlalchemy.exc import IntegrityError

# Cria hash da senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
senha_plana = "admin"
senha_hash = pwd_context.hash(senha_plana)

# Cria sessão
session = Session(bind=engine)

# Cria usuário
novo_usuario = User(email="admin", hashed_password=senha_hash)

# Insere no banco
try:
    session.add(novo_usuario)
    session.commit()
    print("✅ Usuário 'admin' criado com sucesso com senha 'admin'")
except IntegrityError:
    print("⚠️ Usuário 'admin' já existe!")
    session.rollback()
finally:
    session.close()
