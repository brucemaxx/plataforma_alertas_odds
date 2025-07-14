// src/components/TabelaAlertas.jsx

const TabelaAlertas = ({ alertas }) => {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white shadow rounded-md">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-2">Time</th>
            <th className="p-2">Mercado</th>
            <th className="p-2">Odd</th>
            <th className="p-2">Data</th>
            <th className="p-2">Hora</th>
          </tr>
        </thead>
        <tbody>
          {alertas.map((alerta, idx) => (
            <tr key={idx} className="border-b text-center">
              <td className="p-2">{alerta.time}</td>
              <td className="p-2">{alerta.mercado}</td>
              <td className="p-2">{alerta.odd}</td>
              <td className="p-2">{alerta.data}</td>
              <td className="p-2">{alerta.hora}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TabelaAlertas;
