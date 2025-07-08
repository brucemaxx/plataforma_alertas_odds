# app/database/operacoes_alerta.py

from sqlalchemy.orm import Session
from app.models.alerta import Alerta
from app.database.conexao import SessionLocal

def salvar_alerta(dados_alerta: dict):
    """
    Salva um alerta no banco de dados se ele ainda não existir.
    :param dados_alerta: Dicionário com as chaves: time_1, time_2, mercado, odd, timestamp
    """
    session: Session = SessionLocal()
    try:
        # Verifica se já existe um alerta igual (mesmo time_1, time_2, mercado e odd)
        existe = session.query(Alerta).filter_by(
            time_1=dados_alerta["time_1"],
            time_2=dados_alerta["time_2"],
            mercado=dados_alerta["mercado"],
            odd=dados_alerta["odd"]
        ).first()

        if not existe:
            alerta = Alerta(**dados_alerta)
            session.add(alerta)
            session.commit()
            print("✅ Alerta salvo no banco de dados.")
        else:
            print("ℹ️ Alerta já existe no banco. Ignorado.")
    except Exception as e:
        print(f"[ERRO] Falha ao salvar alerta no banco: {e}")
        session.rollback()
    finally:
        session.close()
