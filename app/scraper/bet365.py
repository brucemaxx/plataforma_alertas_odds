# app/scraper/bet365.py

from playwright.sync_api import sync_playwright
from app.schemas.jogo import JogoSchema

def coletar_todos_os_jogos():
    """
    Inicia o navegador, acessa o site simplificado da Bet365 e coleta os jogos disponíveis.
    Retorna uma lista de dicionários com time_1, time_2, mercado e odd.
    """
    jogos = []
    

    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch(headless=False)  # Modo headless para testes
            pagina = navegador.new_page()

            # Acessa a versão móvel ou leve da Bet365 (ajuste para o seu caso real)
            pagina.goto("https://www.bet365.com/?op=m")

            # Espera carregar
            pagina.wait_for_timeout(8000)
            
            with open("bet365.html", "w", encoding="utf-8") as f:
                f.write(pagina.content())

            blocos = pagina.locator("div.cpm-ParticipantFixtureDetailsSoccer_Team").all()

            for i in range(0, len(blocos), 2):
                try:
                    time_1 = blocos[i].inner_text().strip()
                    time_2 = blocos[i+1].inner_text().strip()

                    odd_element = pagina.locator("span.cpm-ParticipantOdds_Odds").nth(i // 2)
                    mercado_element = pagina.locator("div.cpm-MarketOddsHeader").nth(i // 2)

                    odd = odd_element.inner_text().strip()
                    mercado = mercado_element.inner_text().strip()

                    jogo = JogoSchema(
                        time_1=time_1,
                        time_2=time_2,
                        mercado=mercado,
                        odd=odd
                    )
                    jogos.append(jogo.dict())

                except Exception as e:
                    print(f"[ERRO] Falha ao capturar um dos jogos: {e}")
                    continue

            navegador.close()

    except Exception as erro_global:
        print(f"[ERRO GERAL NO PLAYWRIGHT] {erro_global}")

    return jogos
