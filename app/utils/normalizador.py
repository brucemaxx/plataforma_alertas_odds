def normalizador_mercado(mercado: str) -> str:
    """
    Normaliza o nome do mercado para padronização na filtragem.
    Converte para minúsculas e remove variações comuns.

    Exemplos:
    - "Resultado Final" -> "resultado final"
    - "Mais de 2.5 Gols" -> "mais de"
    """
    mercado = mercado.lower()

    if "resultado final" in mercado:
        return "resultado final"
    elif "mais de" in mercado:
        return "mais de"
    elif "menos de" in mercado:
        return "menos de"
    else:
        return mercado
