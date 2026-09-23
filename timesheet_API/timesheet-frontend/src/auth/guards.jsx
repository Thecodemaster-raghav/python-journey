import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from './AuthContext.jsx';

export function RequireAuth({ children }) {
  const { isAuthenticated } = useAuth();
  const location = useLocation();
  if (!isAuthenticated) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }
  return children;
}

// UX only — the backend enforces the real admin check.
export function RequireAdmin({ children }) {
  const { user } = useAuth();
  return user?.isAdmin ? children : <Navigate to="/" replace />;
}

// Login/register: once signed in, go where the user was heading (or home).
export function PublicOnly({ children }) {
  const { isAuthenticated } = useAuth();
  const location = useLocation();
  if (isAuthenticated) {
    return <Navigate to={location.state?.from || '/'} replace />;
  }
  return children;
}
