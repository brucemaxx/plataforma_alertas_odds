// src/components/TabelaAlertas.jsx
const TabelaAlertas = ({ alertas, ordenacao, setOrdenacao }) => {
  const alterarordenacao = (campo) => {
    if (ordenacao.campo === campo) {
      setOrdenacao({
        campo,
        direcao: ordenacao.direcao === 'asc' ? 'desc' : 'asc',
      });
    } else {
      setOrdenacao({ campo, direcao: 'asc' });
    }
  };

  const iconeOrdenacao = (campo) => {
    if (ordenacao.campo !== campo) return '↕️';
    return ordenacao.direcao === 'asc' ? '⬆️' : '⬇️';
  };

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white shadow rounded-md">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-2 cursor-pointer" onClick={() => alterarordenacao('time')}>
              Time {iconeOrdenacao('time')}
            </th>
            <th className="p-2 cursor-pointer" onClick={() => alterarordenacao('mercado')}>
              Mercado {iconeOrdenacao('mercado')}
            </th>
            <th className="p-2 cursor-pointer" onClick={() => alterarordenacao('odd')}>
              Odd {iconeOrdenacao('odd')}
            </th>
            <th className="p-2 cursor-pointer" onClick={() => alterarordenacao('data')}>
              Data {iconeOrdenacao('data')}
            </th>
            <th className="p-2 cursor-pointer" onClick={() => alterarordenacao('hora')}>
              Hora {iconeOrdenacao('hora')}
            </th>
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
