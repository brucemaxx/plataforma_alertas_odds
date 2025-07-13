# init_db.py (na raiz do projeto)

# Importe a engine e a Base do seu arquivo db.py
# O caminho 'app.database.db' funciona porque este script será executado da raiz,
# e 'app' será reconhecido como um pacote.
from app.database.db import engine, Base

# **IMPORTANTE:** Importe TODOS os seus módulos de modelo aqui.
# Isso garante que a Base conheça todas as classes que devem ser tabelas no banco de dados.
# Para o seu caso, certifique-se de que app.models.alerta está importado.
from app.models import alerta # Isso faz com que a definição da classe Alerta seja carregada

def initialize_database():
    """
    Cria todas as tabelas definidas nos modelos no banco de dados.
    Esta função deve ser chamada apenas uma vez para configurar o DB.
    """
    print("Iniciando a criação/verificação das tabelas do banco de dados...")
    # Base.metadata.create_all() cria as tabelas se elas não existirem.
    Base.metadata.create_all(bind=engine)
    print("Tabelas do banco de dados verificadas/criadas com sucesso.")

if __name__ == "__main__":
    initialize_database()