// src/components/GraficoEstatisticas.jsx

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Legend,
} from 'recharts';

const GraficoEstatisticas = ({ alertas }) => {
  // Agrupar alertas por mercado
  const dadosPorMercado = alertas.reduce((acc, alerta) => {
    const mercado = alerta.mercado || 'Desconhecido';
    acc[mercado] = (acc[mercado] || 0) + 1;
    return acc;
  }, {});

  // Transformar objeto em array para o gráfico
  const dadosFormatados = Object.entries(dadosPorMercado).map(
    ([mercado, total]) => ({
      mercado,
      total,
    })
  );

  return (
    <div className="bg-white shadow-md rounded-lg p-4">
      <h2 className="text-xl font-semibold mb-4 text-center">Alertas por Mercado</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={dadosFormatados}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="mercado" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Legend />
          <Bar dataKey="total" fill="#3b82f6" name="Total de alertas" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default GraficoEstatisticas;
