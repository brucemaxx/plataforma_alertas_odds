// src/components/Estatisticas.jsx


const Estatisticas = ({ alertas }) => {
  const total = alertas.length;

  const porMercado = alertas.reduce((acc, alerta) => {
    acc[alerta.mercado] = (acc[alerta.mercado] || 0) + 1;
    return acc;
  }, {});

  return (
    <div className="bg-gray-100 p-4 rounded-lg shadow">
      <h2 className="text-xl font-semibold mb-2">Estatísticas</h2>
      <p>Total de alertas: {total}</p>
      <ul className="list-disc ml-5 mt-2">
        {Object.entries(porMercado).map(([mercado, count]) => (
          <li key={mercado}>
            {mercado}: {count}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Estatisticas;
