import { useState, useEffect } from 'react';
import Filtros from './Filtros';
import TabelaAlertas from './TabelaAlertas';
import Estatisticas from './Estatisticas';
import Paginacao from './Paginacao';
import GraficoEstatisticas from './GraficoEstatisticas';
import LogoutButton from './LogoutButton';
import axios from 'axios';
import jwt_decode from 'jwt-decode'; // ✅ Importa função para decodificar o token

export default function Dashboard({ token, setToken }) {
  const [alertas, setAlertas] = useState([]);
  const [filtros, setFiltros] = useState({ time: '', mercado: '', data: '' });
  const [ordenacao, setOrdenacao] = useState({ campo: 'data', direcao: 'desc' });
  const [paginaAtual, setPaginaAtual] = useState(1);
  const [autorizado, setAutorizado] = useState(false);
  const [nomeUsuario, setNomeUsuario] = useState(''); // ✅ Estado para exibir o nome do usuário
  const alertasPorPagina = 10;

  // 🔐 Verifica se o token é válido
  useEffect(() => {
    const verificarToken = async () => {
      try {
        const response = await axios.get('http://localhost:8000/verify_token', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.data.message === 'Token válido') {
          setAutorizado(true);

          // ✅ Extrai nome do usuário do token
          const decoded = jwt_decode(token);
          setNomeUsuario(decoded.sub || 'Usuário');
        } else {
          setAutorizado(false);
        }
      } catch (error) {
        setAutorizado(false);
      }
    };

    verificarToken();
  }, [token]);

  // 📦 Busca dados dos alertas
  useEffect(() => {
    const fetchAlertas = async () => {
      try {
        const response = await axios.get('http://localhost:8000/alertas', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setAlertas(response.data);
      } catch (error) {
        console.error('Erro ao buscar alertas:', error);
      }
    };

    if (autorizado) {
      fetchAlertas();
    }
  }, [autorizado, token]);

  if (!autorizado) {
    return (
      <div className="p-4 text-lg font-semibold text-center text-red-600">
        Acesso negado. Faça login para continuar.
      </div>
    );
  }

  // 🔎 Aplica os filtros
  const alertasFiltrados = alertas.filter((alerta) => {
    const { time, mercado, data } = filtros;
    return (
      (time === '' || alerta.time.includes(time)) &&
      (mercado === '' || alerta.mercado.includes(mercado)) &&
      (data === '' || alerta.data.includes(data))
    );
  });

  // 🔃 Ordena os alertas
  const alertasOrdenados = [...alertasFiltrados].sort((a, b) => {
    const { campo, direcao } = ordenacao;
    if (a[campo] < b[campo]) return direcao === 'asc' ? -1 : 1;
    if (a[campo] > b[campo]) return direcao === 'asc' ? 1 : -1;
    return 0;
  });

  // 📄 Paginação
  const indexInicial = (paginaAtual - 1) * alertasPorPagina;
  const indexFinal = indexInicial + alertasPorPagina;
  const alertasPaginados = alertasOrdenados.slice(indexInicial, indexFinal);
  const totalPaginas = Math.ceil(alertasFiltrados.length / alertasPorPagina);

  const mudarPagina = (novaPagina) => {
    if (novaPagina >= 1 && novaPagina <= totalPaginas) {
      setPaginaAtual(novaPagina);
    }
  };

  // 📤 Exportar para CSV
  const exportarParaCSV = () => {
    const colunas = ['Time', 'Mercado', 'Odd', 'Data', 'Hora'];
    const linhas = alertasOrdenados.map((a) => [
      a.time,
      a.mercado,
      a.odd,
      a.data,
      a.hora,
    ]);
    const conteudoCSV = [
      colunas.join(','),
      ...linhas.map((linha) => linha.join(',')),
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
      {/* 🔝 Cabeçalho com saudação e logout */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold">Dashboard de Alertas</h1>
          <p className="text-gray-600 text-sm">Bem-vindo, {nomeUsuario}</p>
        </div>
        <LogoutButton setToken={setToken} />
      </div>

      {/* 🎯 Filtros, Estatísticas e Gráfico */}
      <Filtros filtros={filtros} setFiltros={setFiltros} />
      <Estatisticas alertas={alertasFiltrados} />
      <GraficoEstatisticas alertas={alertasFiltrados} />

      {/* 📥 Botão de Exportar CSV */}
      <div className="flex justify-end">
        <button
          onClick={exportarParaCSV}
          className="px-4 py-2 bg-green-500 text-white font-medium rounded hover:bg-green-600 transition"
        >
          Exportar CSV
        </button>
      </div>

      {/* 📊 Tabela de alertas */}
      <TabelaAlertas
        alertas={alertasPaginados}
        ordenacao={ordenacao}
        setOrdenacao={setOrdenacao}
      />

      {/* 📚 Paginação */}
      <Paginacao
        paginaAtual={paginaAtual}
        totalPaginas={totalPaginas}
        mudarPagina={mudarPagina}
      />
    </div>
  );
}
