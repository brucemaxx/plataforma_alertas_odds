from playwright.sync_api import sync_playwright
from app.schemas.jogo import JogoSchema

def coletar_todos_os_jogos(pagina=None):
    """
    Captura todos os jogos e odds visíveis no site da Bet365 (versão web simplificada).
    Se 'pagina' for fornecida, usa a instância já aberta do navegador.
    """
    jogos = []

    if not pagina:
        raise ValueError("A página do navegador precisa ser passada como argumento.")

    pagina.wait_for_timeout(8000)

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

    return jogos
