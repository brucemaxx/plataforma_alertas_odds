import { useState } from "react";
import axios from "axios";

export default function Login({ setToken }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/auth/login", {
        username,
        password,
      });

      const token = response.data.access_token;
      localStorage.setItem("token", token);
      setToken(token);
    } catch (err) {
      alert("Login inválido");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 max-w-md mx-auto mt-10 bg-white rounded-xl shadow">
      <h2 className="text-xl font-bold mb-4">Login</h2>
      <input
        type="text"
        placeholder="Usuário"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        className="block w-full mb-2 p-2 border rounded"
      />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="block w-full mb-2 p-2 border rounded"
      />
      <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
        Entrar
      </button>
    </form>
  );
}
