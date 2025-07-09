# app/utils/normalizador.py

def normalizador_mercado(mercado: str) -> str:
    """
    Normaliza o nome do mercado para facilitar filtragens consistentes.
    Remove aspas, espaços extras, transforma em minúsculas.
    Exemplo: "'1" → "resultado final"
    """
    if not mercado or not isinstance(mercado, str):
        return ""

    # Limpeza geral
    mercado = mercado.strip().lower().replace("'", "").replace('"', '')

    if mercado in ["1", "x", "2"]:
        return "resultado final"
    elif "mais de" in mercado:
        return "mais de"
    elif "menos de" in mercado:
        return "menos de"
    
    return mercado
