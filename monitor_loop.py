# monitor_loop.py

import os
import time
from dotenv import load_dotenv
from telegram import Bot
from datetime import datetime
from app.scraper.bet365 import coletar_todos_os_jogos
from app.utils.normalizador import normalizador_mercado
from app.database.db import SessionLocal
from app.database.operacoes_alerta import salvar_alerta
from app.models.alerta import Alerta
from sqlalchemy.exc import SQLAlchemyError

# 📌 Carrega variáveis do .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MERCADOS_DESEJADOS = os.getenv("MERCADOS_DESEJADOS", "")
MIN_ODD = float(os.getenv("MIN_ODD", "3.00"))
INTERVALO = int(os.getenv("INTERVALO", "60"))  # segundos

# 🤖 Bot do Telegram
bot = Bot(token=TELEGRAM_TOKEN)

# 🧠 Para evitar alertas duplicados
alertas_enviados = set()

def enviar_alerta_telegram(alerta_dados: dict):
    """Envia mensagem formatada para o Telegram."""
    mensagem = (
        f"⚽ *Alerta de Odd!*\n\n"
        f"🏟️ {alerta_dados['time_1']} x {alerta_dados['time_2']}\n"
        f"📊 Mercado: {alerta_dados['mercado']}\n"
        f"💰 Odd: *{alerta_dados['odd']}*"
    )
    bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode="Markdown")

def monitorar_jogos():
    """Loop contínuo para capturar, filtrar, alertar e salvar dados."""

    print("🚀 Monitoramento iniciado!")
    print("🎯 Mercados desejados:", MERCADOS_DESEJADOS)
    lista_mercados = [m.strip().lower() for m in MERCADOS_DESEJADOS.split(",") if m.strip()]
    
    while True:
        jogos = coletar_todos_os_jogos()

        if not jogos:
            print("[⛔] Nenhum jogo capturado.")
            time.sleep(INTERVALO)
            continue

        for dados in jogos:
            try:
                # Validação básica
                if len(dados["mercado"].strip()) <= 1:
                    print(f"[IGNORADO] Mercado vazio ou inválido: '{dados['mercado']}")
                    continue

                mercado_nome = normalizador_mercado(dados["mercado"])
                if lista_mercados and mercado_nome not in lista_mercados:
                    print(f"[IGNORADO] Mercado não desejado: {dados['mercado']} não está na lista desejada.")
                    continue

                # Conversão da odd
                odd = float(dados["odd"].replace(",", "."))
                if odd < MIN_ODD:
                    print(f"[IGNORADO] Odd {odd} abaixo do mínimo.")
                    continue

                # Verificação de duplicata
                chave_alerta = f"{dados['time_1']}|{dados['time_2']}|{dados['mercado']}|{dados['odd']}"
                if chave_alerta in alertas_enviados:
                    print("[DUPLICADO] Alerta já enviado:", chave_alerta)
                    continue

                # Criação do alerta
                alerta_dados = {
                    "time_1": dados["time_1"],
                    "time_2": dados["time_2"],
                    "mercado": dados["mercado"],
                    "odd": dados["odd"],
                    "data_envio": datetime.utcnow()
                }

                # Envia e salva
                enviar_alerta_telegram(alerta_dados)
                db = SessionLocal()
                salvar_alerta(db, alerta_dados)
                db.close()

                print(f"[✅] Alerta enviado e salvo: {chave_alerta}")
                alertas_enviados.add(chave_alerta)

            except SQLAlchemyError as db_err:
                print(f"[DB ERRO] {db_err}")
            except Exception as e:
                print(f"[ERRO GERAL] {e}")

        print(f"⏳ Aguardando {INTERVALO} segundos...\n")
        time.sleep(INTERVALO)

# 🔁 Ponto de entrada
if __name__ == "__main__":
    monitorar_jogos()
