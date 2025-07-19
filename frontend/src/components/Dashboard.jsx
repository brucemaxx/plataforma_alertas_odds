// src/components/Dashboard.jsx
import { useState, useEffect } from 'react';
import Filtros from './Filtros';
import TabelaAlertas from './TabelaAlertas';
import Estatisticas from './Estatisticas';
import Paginacao from './Paginacao'; // ✅ importar novo componente
import GraficoEstatisticas from './GraficoEstatisticas'; // Importar o novo componente de gráfico
import axios from 'axios';


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

  const exportarParaCSV = () => {
  const colunas = ['Time', 'Mercado', 'Odd', 'Data', 'Hora'];

  const linhas = alertasOrdenados.map((alerta) => [
    alerta.time,
    alerta.mercado,
    alerta.odd,
    alerta.data,
    alerta.hora,
  ]);

  const conteudoCSV = [
    colunas.join(','),           // Cabeçalho
    ...linhas.map((linha) => linha.join(',')) // Linhas de dados
  ].join('\n');

  const blob = new Blob([conteudoCSV], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `alertas_${new Date().toISOString().slice(0, 10)}.csv`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};


  return (
    <div className="p-4 space-y-6">
      <h1 className="text-3xl font-bold text-center">Dashboard de Alertas</h1>

      <Filtros filtros={filtros} setFiltros={setFiltros} />

      <Estatisticas alertas={alertasFiltrados} />

      <GraficoEstatisticas alertas={alertasFiltrados}/>

      <div className="flex justify-end">
        <button
          onClick={exportarParaCSV}
          className="px-4 py-2 bg-green-500 text-white font-medium rounded hover:bg-green-600 transition"
        >
        Exportar CSV
        </button>
      </div>



      <TabelaAlertas
       alertas={alertasPaginados}
       ordenacao={ordenacao}
       setOrdenacao={setOrdenacao}
      />

      {/* ✅ Componente isolado de paginação */}
      <Paginacao
        paginaAtual={paginaAtual}
        totalPaginas={totalPaginas}
        mudarPagina={mudarPagina}
      />
    </div>
  );
};

// export default Dashboard;

export default function Dashboard({token}) {
  const [mensagem, setMensagem] = useState('');

  useEffect(() => {
    const verificarToken = async () => {
      try {
        const response = await axios.get('http://localhost:8000/verify_token', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        setMensagem(response.data.message);
      } catch (error) {
        setMensagem("Acesso negado");
      }
    };

    fetchData();
  }, [token]);

  return (
    <div className="p-4 text-lg font-semibold text-center">
      {mensagem}
    </div>
  );
}

