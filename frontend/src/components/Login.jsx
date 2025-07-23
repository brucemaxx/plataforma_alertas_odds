// src/components/Login.jsx

import { useState } from "react";
import axios from "axios";

export default function Login({ setToken }) {
  const [credentials, setCredentials] = useState({
    username: "",
    password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:8000/auth/login", {
        username: credentials.username,
        password: credentials.password,
      });

      const token = response.data.access_token;
      localStorage.setItem("token", token);
      setToken(token);
    } catch (err) {
      const mensagemErro = err.response?.data?.detail || "Erro no login. Tente novamente.";
      alert(mensagemErro);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="p-4 max-w-md mx-auto mt-10 bg-white rounded-xl shadow"
    >
      <h2 className="text-xl font-bold mb-4 text-center">Login</h2>

      <input
        type="text"
        name="username"
        placeholder="Usuário"
        value={credentials.username}
        onChange={handleChange}
        required
        autoComplete="username"
        aria-label="Usuário"
        className="block w-full mb-3 p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
      />

      <input
        type="password"
        name="password"
        placeholder="Senha"
        value={credentials.password}
        onChange={handleChange}
        required
        autoComplete="current-password"
        aria-label="Senha"
        className="block w-full mb-4 p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
      />

      <button
        type="submit"
        className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 transition"
      >
        Entrar
      </button>
    </form>
  );
}
