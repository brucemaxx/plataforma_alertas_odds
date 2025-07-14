# init_db.py (LOCALIZAÇÃO: C:\Users\Windows\OneDrive\Área de Trabalho\plataforma_alertas_odds\init_db.py)

# Importe a engine e a Base do seu arquivo db.py
# O Python consegue resolver 'app.database.db' porque este script está na raiz do projeto.
from app.database.db import engine, Base

# *** IMPORTANTE ***
# Você deve importar TODOS os seus módulos de modelo AQUI!
# Cada módulo de modelo que contém uma classe que herda de `Base`
# precisa ser importado para que `Base.metadata.create_all()` saiba
# que deve criar uma tabela para essa classe.
from app.models import alerta # Isto carrega a definição da classe Alerta na memória

def initialize_database():
    """
    Cria todas as tabelas definidas nos modelos no banco de dados.
    Esta função deve ser chamada apenas uma vez para configurar o DB.
    """
    print("\n--- Iniciando a criação/verificação das tabelas do banco de dados ---")
    # Este comando cria as tabelas se elas AINDA NÃO EXISTIREM no arquivo DB.
    Base.metadata.create_all(bind=engine)
    print("--- Tabelas do banco de dados verificadas/criadas com sucesso ---\n")

if __name__ == "__main__":
    initialize_database()