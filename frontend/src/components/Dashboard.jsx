import React, { useEffect, useState } from "react";

export default function Dashboard() {
  const [alertas, setAlertas] = useState([]);
  const [filtros, setFiltros] = useState({
    time: "",
    mercado: "",
    data: ""
  });

  const [stats, setStats] = useState({
    total: 0,
    mediaOdds: 0,
    porMercado: {}
  });

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch("http://localhost:8000/alertas");
        const data = await res.json();
        setAlertas(data);
        calcularEstatisticas(data);
      } catch (err) {
        console.error("Erro ao buscar dados:", err);
      }
    }

    fetchData();
  }, []);

  const calcularEstatisticas = (dados) => {
    const total = dados.length;
    const somaOdds = dados.reduce((acc, alerta) => acc + parseFloat(alerta.odd), 0);
    const mediaOdds = total > 0 ? (somaOdds / total).toFixed(2) : 0;

    const porMercado = {};
    dados.forEach((alerta) => {
      const mercado = alerta.mercado.toLowerCase();
      porMercado[mercado] = (porMercado[mercado] || 0) + 1;
    });

    setStats({ total, mediaOdds, porMercado });
  };

  const alertasFiltrados = alertas.filter((a) => {
    return (
      (filtros.time === "" ||
        a.time_1.toLowerCase().includes(filtros.time.toLowerCase()) ||
        a.time_2.toLowerCase().includes(filtros.time.toLowerCase())) &&
      (filtros.mercado === "" ||
        a.mercado.toLowerCase().includes(filtros.mercado.toLowerCase())) &&
      (filtros.data === "" || a.data_envio.startsWith(filtros.data))
    );
  });

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">📊 Dashboard de Alertas</h1>

      {/* Filtros */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <input
          type="text"
          placeholder="Filtrar por time"
          className="border rounded px-4 py-2"
          value={filtros.time}
          onChange={(e) => setFiltros({ ...filtros, time: e.target.value })}
        />
        <input
          type="text"
          placeholder="Filtrar por mercado"
          className="border rounded px-4 py-2"
          value={filtros.mercado}
          onChange={(e) => setFiltros({ ...filtros, mercado: e.target.value })}
        />
        <input
          type="date"
          className="border rounded px-4 py-2"
          value={filtros.data}
          onChange={(e) => setFiltros({ ...filtros, data: e.target.value })}
        />
      </div>

      {/* Estatísticas */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div className="bg-white shadow rounded p-4">
          <h2 className="font-semibold">Total de Alertas</h2>
          <p className="text-2xl">{stats.total}</p>
        </div>
        <div className="bg-white shadow rounded p-4">
          <h2 className="font-semibold">Média de Odds</h2>
          <p className="text-2xl">{stats.mediaOdds}</p>
        </div>
        <div className="bg-white shadow rounded p-4">
          <h2 className="font-semibold">Por Mercado</h2>
          <ul className="text-sm">
            {Object.entries(stats.porMercado).map(([mercado, qtd]) => (
              <li key={mercado}>
                {mercado}: {qtd}
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Tabela de alertas */}
      <table className="w-full table-auto border">
        <thead>
          <tr className="bg-gray-100 text-left">
            <th className="border px-4 py-2">Time 1</th>
            <th className="border px-4 py-2">Time 2</th>
            <th className="border px-4 py-2">Mercado</th>
            <th className="border px-4 py-2">Odd</th>
            <th className="border px-4 py-2">Data</th>
          </tr>
        </thead>
        <tbody>
          {alertasFiltrados.map((a, i) => (
            <tr key={i} className="hover:bg-gray-50">
              <td className="border px-4 py-2">{a.time_1}</td>
              <td className="border px-4 py-2">{a.time_2}</td>
              <td className="border px-4 py-2">{a.mercado}</td>
              <td className="border px-4 py-2">{a.odd}</td>
              <td className="border px-4 py-2">
                {new Date(a.data_envio).toLocaleString()}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
