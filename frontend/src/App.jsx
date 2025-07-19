import Login from "./components/Login";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <div className="bg-gray-50 min-h-screen">
      <Dashboard />
    </div>
  );
}

// Controlando o estado do token de autenticação.
// Se o token estiver presente, renderiza o Dashboard, caso contrário, renderiza o Login.
function App() {
  const [token, setToken] = userState(localStorage.getItem("token"));

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  return (
    <div>
      {token ? (
        < >
        <button onClick={handleLogout} className="m-4 bg-red-500 text-white p-2 rounded hover:bg-red-600">
          Sair
        </button>
        <Dashboard token={token} />
        </>
      ) : (
        <Login setToken={setToken} />
      )}
    </div>
  );
}

export default App;