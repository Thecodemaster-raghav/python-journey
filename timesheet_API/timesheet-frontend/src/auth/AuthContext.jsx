import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api, setUnauthorizedHandler, tokenStore } from '../api.js';
import { decodeJwt, isExpired, readIdentity } from './claims.js';

const AuthContext = createContext(null);

function loadStoredToken() {
  const token = tokenStore.get();
  if (!token) return null;
  const claims = decodeJwt(token);
  if (!claims || isExpired(claims)) {
    tokenStore.clear();
    return null;
  }
  return token;
}

export function AuthProvider({ children }) {
  const navigate = useNavigate();
  const [token, setToken] = useState(loadStoredToken);

  const user = useMemo(() => (token ? readIdentity(decodeJwt(token)) : null), [token]);

  // Ends the session locally and sends the user to login with a reason to show.
  const endSession = useCallback(
    (reason) => {
      tokenStore.clear();
      setToken(null);
      navigate('/login', { replace: true, state: reason ? { reason } : undefined });
    },
    [navigate]
  );

  // Any 401/403 from a protected call lands here (see api.js).
  useEffect(() => {
    setUnauthorizedHandler(() => endSession('expired'));
    return () => setUnauthorizedHandler(null);
  }, [endSession]);

  const login = useCallback(async (username, password) => {
    const data = await api.login({ username, password });
    if (!data?.access_token) throw new Error('No token in login response.');
    tokenStore.set(data.access_token);
    setToken(data.access_token);
  }, []);

  const logout = useCallback(() => endSession(), [endSession]);

  const value = useMemo(
    () => ({ user, isAuthenticated: Boolean(user), login, logout, endSession }),
    [user, login, logout, endSession]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used inside <AuthProvider>.');
  return ctx;
}
