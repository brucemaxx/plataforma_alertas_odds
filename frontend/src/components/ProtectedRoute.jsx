// scr/components/ProtectedRoute.jsx
import {Navigate} from "react-router-dom";

const ProtectedRoute = ({children}) => {
    const token = localStorage.getItem("token");

    // Se não houver token, rediriciona para a tela de login
    if (!token) {
        return <Navigate to="/login" replace/>;
    }

    // Se houver token, exibe o componente filho (ex: dashboard)
    return children;
};

export default ProtectedRoute;