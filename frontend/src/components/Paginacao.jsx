// src/components/Paginacao.jsx


const Paginacao = ({ paginaAtual, totalPaginas, mudarPagina }) => {
  return (
    <div className="flex justify-center items-center gap-2 mt-4">
      <button
        onClick={() => mudarPagina(paginaAtual - 1)}
        className="px-3 py-1 bg-gray-200 hover:bg-gray-300 rounded disabled:opacity-50"
        disabled={paginaAtual === 1}
      >
        Anterior
      </button>

      <span className="px-4 font-medium">
        Página {paginaAtual} de {totalPaginas}
      </span>

      <button
        onClick={() => mudarPagina(paginaAtual + 1)}
        className="px-3 py-1 bg-gray-200 hover:bg-gray-300 rounded disabled:opacity-50"
        disabled={paginaAtual === totalPaginas}
      >
        Próxima
      </button>
    </div>
  );
};

export default Paginacao;
