// src/components/Filtros.jsx

const Filtros = ({ filtros, setFiltros }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFiltros((prev) => ({ ...prev, [name]: value }));
  };

  const limparFiltros = () => {
    setFiltros({ time: '', mercado: '', data: '' });
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
      <input
        type="text"
        name="time"
        placeholder="Filtrar por time"
        value={filtros.time}
        onChange={handleChange}
        aria-label="Filtrar por time"
        className="p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
      />
      <input
        type="text"
        name="mercado"
        placeholder="Filtrar por mercado"
        value={filtros.mercado}
        onChange={handleChange}
        aria-label="Filtrar por mercado"
        className="p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
      />
      <input
        type="date"
        name="data"
        value={filtros.data}
        onChange={handleChange}
        aria-label="Filtrar por data"
        className="p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
      />

      <button
        onClick={limparFiltros}
        className="md:col-span-3 p-2 bg-red-500 text-white rounded-md hover:bg-red-600 transition"
      >
        Limpar filtros
      </button>
    </div>
  );
};

export default Filtros;
