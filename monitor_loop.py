# monitor_loop.py

import time
import os
from telegram import Bot
from dotenv import load_dotenv, dotenv_values

# 🔧 Importa função do scraper e normalizador de mercados
from app.scraper.bet365 import coletar_todos_os_jogos
from app.utils.normalizador import normalizador_mercado

# 📦 Importações para banco de dados
from app.database.db import SessionLocal
from app.models.alerta import Alerta

from app.database.operacoes_alerta import salvar_alerta
from datetime import datetime

# 🧪 Carrega variáveis do .env (token, chat_id, mercados, etc.)
load_dotenv()
valores = dotenv_values()
print("✅ VALORES CARREGADOS DO .env:", valores)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MERCADOS = os.getenv("MERCADOS_DESEJADOS", "")
MIN_ODD = float(os.getenv("MIN_ODD", "3.00"))  # Odd mínima vinda do .env

# 🤖 Instancia o bot
print("🎯 TOKEN:", TOKEN)
print("💬 CHAT_ID:", CHAT_ID)
bot = Bot(token=TOKEN)

# ⏱️ Tempo entre as varreduras (em segundos)
INTERVALO = 60

# 🚫 Armazena alertas já enviados para evitar duplicatas
alertas_enviados = set()
"""
def monitorar_jogos():
    '''
    Função principal que coleta jogos, filtra por odd e mercado desejado,
    envia alertas e salva no banco de dados.
    '''

    # 🧹 Normaliza e prepara lista de mercados desejados
    lista_mercados = [m.strip().lower() for m in MERCADOS.split(",") if m.strip()]
    print(f"🎯 Monitorando apenas os mercados: {lista_mercados}")

    # 🔄 Cria sessão com o banco de dados (SQLAlchemy)
    session = SessionLocal()

    while True:
        jogos = coletar_todos_os_jogos()

        if not jogos:
            print("[AVISO] Nenhum jogo capturado.")
        else:
            for dados in jogos:
                try:
                    # 🔎 Ignora mercados com texto curto como "1", "X", "2"
                    if len(dados["mercado"].strip()) <= 2:
                        print(f"[IGNORADO] Mercado inválido: {dados['mercado']}")
                        continue

                    # 🔤 Normaliza nome do mercado
                    mercado_nome = normalizador_mercado(dados["mercado"])

                    # 🔁 Se houver mercados definidos, verifica se é desejado
                    if lista_mercados and mercado_nome not in lista_mercados:
                        print(f"[IGNORADO] Mercado não desejado: {dados['mercado']}, não está na lista de mercados desejados")
                        continue

                    # 💰 Verifica se a odd atende o mínimo exigido
                    odd = float(dados["odd"].replace(",", "."))

                    if odd >= MIN_ODD:
                        chave_alerta = f"{dados['time_1']} x {dados['time_2']} - {dados['mercado']} - {dados['odd']}"

                        if chave_alerta not in alertas_enviados:
                            # 📨 Envia mensagem para o Telegram
                            mensagem = (
                                f"🎯 *Alerta de Odd!*\n\n"
                                f"🏟️ {dados['time_1']} x {dados['time_2']}\n"
                                f"📊 Mercado: {dados['mercado']}\n"
                                f"💰 Odd: *{dados['odd']}*"
                            )
                            bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode="Markdown")
                            print("[ALERTA] Enviado:", chave_alerta)
                            
                        
                            # 💾 Salva alerta no banco
                            alerta = Alerta(
                                time_1=dados["time_1"],
                                time_2=dados["time_2"],
                                mercado=dados["mercado"],
                                odd=dados["odd"]
                            )
                            session.add(alerta)
                            session.commit()

                            dados_para_salvar = {
                                "Time_1": dados["time_1"],
                                "time_2": dados["time_2"],
                                "mercado": dados["meracdo"],
                                "odd": dados["odd"],
                                "timestamp": datetime.now()
                            }
                            salvar_alerta(dados_para_salvar)
                            
                            
                    
                            
                            
                            # ✅ Marca como já enviado
                            alertas_enviados.add(chave_alerta)
                        else:
                            print("[IGNORADO] Alerta já enviado:", chave_alerta)
                    else:
                        print(f"[INFO] {dados['time_1']} x {dados['time_2']} | Odd {odd} abaixo do limite")

                except Exception as e:
                    print(f"[ERRO] Falha ao processar jogo: {e}")

        # ⏱️ Aguarda até a próxima rodada
        time.sleep(INTERVALO)

    # 🧹 Encerra sessão com o banco ao final (caso saia do loop)
    session.close()


# 🚀 Ponto de entrada do script
if __name__ == "__main__":
    monitorar_jogos()
"""

from app.database.conexao import SessionLocal
from app.models.alerta import Alerta

# ... (mantém os imports e definições acima como estão)

def monitorar_jogos():
    mercados_desejados = os.getenv("MERCADOS_DESEJADOS", "")
    lista_mercados = [m.strip().lower() for m in mercados_desejados.split(",") if m.strip()]
    print(f"🎯 Monitorando apenas os mercados: {lista_mercados}")

    while True:
        jogos = coletar_todos_os_jogos()

        if not jogos:
            print("[AVISO] Nenhum jogo capturado.")
        else:
            for dados in jogos:
                try:
                    if len(dados["mercado"].strip()) <= 2:
                        print(f"[IGNORADO] Mercado inválido: {dados['mercado']}")
                        continue
                    
                    mercado_nome = normalizador_mercado(dados["mercado"])
                    if lista_mercados and mercado_nome not in lista_mercados:
                        print(f"[IGNORADO] Mercado não desejado: {dados['mercado']}, não está na lista.")
                        continue
                    
                    odd = float(dados["odd"].replace(",", "."))

                    if odd >= MIN_ODD:
                        chave_alerta = f"{dados['time_1']} x {dados['time_2']} - {dados['mercado']} - {dados['odd']}"

                        if chave_alerta not in alertas_enviados:
                            mensagem = (
                                f"🎯 *Alerta de Odd!*\n\n"
                                f"🏟️ {dados['time_1']} x {dados['time_2']}\n"
                                f"📊 Mercado: {dados['mercado']}\n"
                                f"💰 Odd: *{dados['odd']}*"
                            )
                            bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode="Markdown")
                            alertas_enviados.add(chave_alerta)

                            # 👉 Persistir no banco
                            db = SessionLocal()
                            novo_alerta = Alerta(
                                time_1=dados['time_1'],
                                time_2=dados['time_2'],
                                mercado=dados['mercado'],
                                odd=dados['odd']
                            )
                            db.add(novo_alerta)
                            db.commit()
                            db.close()

                            print("[ALERTA] Enviado e salvo no banco:", chave_alerta)
                        else:
                            print("[IGNORADO] Alerta já enviado:", chave_alerta)
                    else:
                        print(f"[INFO] {dados['time_1']} x {dados['time_2']} | Odd {odd} abaixo do limite")
                except Exception as e:
                    print(f"[ERRO] Falha ao processar jogo: {e}")
