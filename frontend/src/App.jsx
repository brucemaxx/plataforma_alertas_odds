// src/App.jsx
import { useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
// import Login from "./components/Login";
// import Dashboard from "./components/Dashboard";

export default function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "");

  return (
    <BrowserRouter>
      <Routes>
        {/* Acesso direto ao dashboard */}
        <Route
          path="/"
          element={token ? <Navigate to="/dashboard" /> : <Navigate to="/login" />}
        />


        {/* Rotas para Login e Dashboard */}
        {/* <Route path="/login" element={<Login setToken={setToken} />} /> */}
        {/* <Route path="/dashboard" element={token ? <Dashboard token={token}setToken={setToken} /> : <Navigate to="/login" />
          }
        />*/}
      </Routes>
    </BrowserRouter>
  );
}
