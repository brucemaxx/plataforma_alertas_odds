# monitor_loop.py

import os
import time
from dotenv import load_dotenv
from telegram import Bot
from datetime import datetime
from app.database.db import SessionLocal
from app.models.alerta import Alerta
from app.utils.normalizador import normalizador_mercado
from app.scraper.bet365 import coletar_todos_os_jogos
from playwright.sync_api import sync_playwright, Page
from sqlalchemy.exc import SQLAlchemyError

# Carrega variáveis do ambiente
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MERCADOS_DESEJADOS = os.getenv("MERCADOS_DESEJADOS", "").lower().split(",")
MIN_ODD = float(os.getenv("MIN_ODD", "3.00"))

bot = Bot(token=TELEGRAM_TOKEN)
INTERVALO = 60
alertas_enviados = set()

def enviar_telegram(alerta: dict):
    msg = (
        f"🎯 *Alerta de Odd!*\n\n"
        f"🏟️ {alerta['time_1']} x {alerta['time_2']}\n"
        f"📊 Mercado: {alerta['mercado']}\n"
        f"💰 Odd: *{alerta['odd']}*"
    )
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg, parse_mode="Markdown")

def monitorar_jogos():
    print("🚀 Monitoramento iniciado!")
    print(f"🎯 Mercados desejados: {', '.join(MERCADOS_DESEJADOS)}")

    with sync_playwright() as p:
        navegador = p.firefox.launch(headless=False)
        pagina = navegador.new_page()
        pagina.goto("https://www.bet365.com/#/AC/B1/C1/D8/E145283/F2/")

        while True:
            jogos = coletar_todos_os_jogos(pagina)

            if not jogos:
                print("⛔ Nenhum jogo capturado!")
            else:
                db = SessionLocal()
                for jogo in jogos:
                    try:
                        mercado_normalizado = normalizador_mercado(jogo["mercado"])
                        if not mercado_normalizado or len(mercado_normalizado) < 4:
                            print(f"[IGNORADO] Mercado vazio ou inválido: '{jogo['mercado']}'")
                            continue

                        if mercado_normalizado not in [m.strip() for m in MERCADOS_DESEJADOS]:
                            print(f"[IGNORADO] Mercado não desejado: {mercado_normalizado} não está na lista desejada.")
                            continue

                        odd = float(jogo["odd"].replace(",", "."))
                        if odd < MIN_ODD:
                            continue

                        chave = f"{jogo['time_1']}|{jogo['time_2']}|{jogo['mercado']}|{jogo['odd']}"
                        if chave in alertas_enviados:
                            continue

                        # Envia alerta
                        enviar_telegram(jogo)

                        # Salva no banco
                        novo_alerta = Alerta(
                            time_1=jogo["time_1"],
                            time_2=jogo["time_2"],
                            mercado=jogo["mercado"],
                            odd=jogo["odd"],
                            data_envio=datetime.utcnow()
                        )
                        db.add(novo_alerta)
                        db.commit()

                        print(f"[✅] Alerta enviado e salvo: {chave}")
                        alertas_enviados.add(chave)

                    except SQLAlchemyError as err:
                        print(f"[DB ERRO] {err}")
                    except Exception as e:
                        print(f"[ERRO] Falha ao processar jogo: {e}")
                db.close()

            print("⏳ Aguardando 60 segundos...")
            time.sleep(INTERVALO)

if __name__ == "__main__":
    monitorar_jogos()
