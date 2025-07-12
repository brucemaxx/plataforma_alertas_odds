# create_db.py

# Importe a engine e a Base do seu arquivo db.py
from app.database.db import engine, Base

# **IMPORTANTE:** Você precisa importar TODOS os seus modelos SQLAlchemy
# aqui para que Base.metadata.create_all() os "veja" e crie as tabelas.
# Por exemplo, se você tem um modelo Alerta em app/models/alerta.py:
from app.models import alerta # Isso importa o módulo, tornando o Alerta visível para Base

def create_tables():
    print("Tentando criar tabelas do banco de dados...")
    # Isso cria todas as tabelas que foram definidas usando 'Base' e que foram importadas.
    Base.metadata.create_all(bind=engine)
    print("Verificação de tabelas concluída. Tabelas existentes ou criadas.")

if __name__ == "__main__":
    create_tables()