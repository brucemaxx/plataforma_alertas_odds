// src/components/Filtros.jsx


const Filtros = ({ filtros, setFiltros }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFiltros((prev) => ({ ...prev, [name]: value }));
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <input
        type="text"
        name="time"
        placeholder="Filtrar por time"
        value={filtros.time}
        onChange={handleChange}
        className="p-2 border rounded-md"
      />
      <input
        type="text"
        name="mercado"
        placeholder="Filtrar por mercado"
        value={filtros.mercado}
        onChange={handleChange}
        className="p-2 border rounded-md"
      />
      <input
        type="date"
        name="data"
        value={filtros.data}
        onChange={handleChange}
        className="p-2 border rounded-md"
      />
    </div>
  );
};

export default Filtros;
