# testar_scraper_visual.py

from playwright.sync_api import sync_playwright
from app.scraper.bet365 import coletar_todos_os_jogos
from pprint import pprint

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=100)
    pagina = navegador.new_page()
    pagina.goto("https://www.bet365.com/#/HO/")

    input("🟡 Pressione Enter após interagir e posicionar a página...\n")

    try:
        jogos = coletar_todos_os_jogos(pagina)
        print(f"✅ {len(jogos)} jogos capturados:")
        pprint(jogos)
    except Exception as e:
        print(f"[ERRO] Falha ao coletar os jogos: {e}")

    input("✅ Pressione Enter para encerrar e fechar o navegador.")
    navegador.close()
