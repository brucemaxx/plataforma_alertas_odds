import { useNavigate } from "react-router-dom";

export default function LogoutButton({ setToken }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Remove o token do localStorage
    localStorage.removeItem("token");

    // Limpa o token do estado global (App.jsx)
    setToken("");

    // Redireciona para a página de login
    navigate("/login");
  };

  //return (
  //  <button
  //    onClick={handleLogout}
  //    className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-xl shadow-md transition duration-200"
  //  >
  //    Sair
  //  </button>
  //);
}
