// src/components/Dashboard.jsx
import { useState, useEffect } from 'react';
import Filtros from './Filtros';
import TabelaAlertas from './TabelaAlertas';
import Estatisticas from './Estatisticas';
import Paginacao from './Paginacao'; // ✅ importar novo componente
import GraficoEstatisticas from './GraficoEstatisticas' // Importar o novo componente de gráfico

const Dashboard = () => {
  const [alertas, setAlertas] = useState([]);
  const [filtros, setFiltros] = useState({ time: '', mercado: '', data: '' });
  
  const [ordenacao, setOrdenacao] = useState({ campo: 'data', direcao: 'desc' });

  const [paginaAtual, setPaginaAtual] = useState(1);
  const alertasPorPagina = 10;

  // estados de ordenação
  const [ordenarPor, setOdenarPor] = useState('');
  const [ordemCrescente, setOrdemCrescente] =useState(true);

  useEffect(() => {
    const fetchAlertas = async () => {
      try {
        const response = await fetch('http://localhost:8000/alertas');
        const data = await response.json();
        setAlertas(data);
      } catch (error) {
        console.error('Erro ao buscar alertas:', error);
      }
    };

    fetchAlertas();
  }, []);

  const alertasFiltrados = alertas.filter((alerta) => {
    const { time, mercado, data } = filtros;
    return (
      (time === '' || alerta.time.includes(time)) &&
      (mercado === '' || alerta.mercado.includes(mercado)) &&
      (data === '' || alerta.data.includes(data))
    );
  });

  // ORDENAR alertas após aplicar os filtros
  const alertasOrdenados = [...alertasFiltrados].sort((a, b) => {
    const { campo, direcao } = ordenacao;

    if(a[campo] < b[campo]) return direcao === 'asc' ? -1 : 1;
    if(a[campo] > b[campo]) return direcao === 'asc' ? 1 : -1;
    return 0;
  });


  const indexInicial = (paginaAtual - 1) * alertasPorPagina;
  const indexFinal = indexInicial + alertasPorPagina;
  const alertasPaginados = alertasOrdenados.slice(indexInicial, indexFinal);

  const totalPaginas = Math.ceil(alertasFiltrados.length / alertasPorPagina);

  const mudarPagina = (novaPagina) => {
    if (novaPagina >= 1 && novaPagina <= totalPaginas) {
      setPaginaAtual(novaPagina);
    }
  };

  return (
    <div className="p-4 space-y-6">
      <h1 className="text-3xl font-bold text-center">Dashboard de Alertas</h1>

      <Filtros filtros={filtros} setFiltros={setFiltros} />

      <Estatisticas alertas={alertasFiltrados} />

      <GraficoEstatisticas alertas={alertasFiltrados}/>

      <TabelaAlertas alertas={alertasPaginados} />

      {/* ✅ Componente isolado de paginação */}
      <Paginacao
        paginaAtual={paginaAtual}
        totalPaginas={totalPaginas}
        mudarPagina={mudarPagina}
      />
    </div>
  );
};

export default Dashboard;
