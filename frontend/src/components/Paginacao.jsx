// src/components/Paginacao.jsx

const Paginacao = ({ paginaAtual, totalPaginas, mudarPagina }) => {
  const MAX_PAGINAS_VISIVEIS = 5;

  const gerarNumerosPaginas = () => {
    const paginas = [];
    let inicio = Math.max(1, paginaAtual - Math.floor(MAX_PAGINAS_VISIVEIS / 2));
    let fim = inicio + MAX_PAGINAS_VISIVEIS - 1;

    if (fim > totalPaginas) {
      fim = totalPaginas;
      inicio = Math.max(1, fim - MAX_PAGINAS_VISIVEIS + 1);
    }

    for (let i = inicio; i <= fim; i++) {
      paginas.push(i);
    }

    return paginas;
  };

  return (
    <div className="flex flex-wrap justify-center items-center gap-2 mt-6">
      {/* Botão Início */}
      <button
        onClick={() => mudarPagina(1)}
        className="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300 disabled:opacity-50"
        disabled={paginaAtual === 1}
      >
        &laquo;
      </button>

      {/* Botão Anterior */}
      <button
        onClick={() => mudarPagina(paginaAtual - 1)}
        className="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300 disabled:opacity-50"
        disabled={paginaAtual === 1}
      >
        &lt;
      </button>

      {/* Números das páginas */}
      {gerarNumerosPaginas().map((pagina) => (
        <button
          key={pagina}
          onClick={() => mudarPagina(pagina)}
          className={`px-3 py-1 rounded font-medium ${
            pagina === paginaAtual
              ? 'bg-blue-500 text-white'
              : 'bg-gray-100 hover:bg-gray-200'
          }`}
        >
          {pagina}
        </button>
      ))}

      {/* Botão Próxima */}
      <button
        onClick={() => mudarPagina(paginaAtual + 1)}
        className="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300 disabled:opacity-50"
        disabled={paginaAtual === totalPaginas}
      >
        &gt;
      </button>

      {/* Botão Fim */}
      <button
        onClick={() => mudarPagina(totalPaginas)}
        className="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300 disabled:opacity-50"
        disabled={paginaAtual === totalPaginas}
      >
        &raquo;
      </button>
    </div>
  );
};

export default Paginacao;
