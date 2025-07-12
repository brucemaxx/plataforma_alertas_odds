# initialize_db.py
from app.database.db import engine, Base
from app.models import alerta # Importe todos os seus modelos aqui!

def create_tables():
    print("Criando tabelas do banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    create_tables()