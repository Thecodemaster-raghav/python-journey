import { NavLink, Outlet } from 'react-router-dom';
import { useAuth } from '../auth/AuthContext.jsx';
import { Brand } from './ui.jsx';

export default function Layout() {
  const { user, logout } = useAuth();

  return (
    <>
      <header className="topbar">
        <div className="topbar-inner">
          <Brand />
          <nav className="nav" aria-label="Main">
            <NavLink to="/" end>Dashboard</NavLink>
            {user?.isAdmin && <NavLink to="/admin">Admin</NavLink>}
            <NavLink to="/account">Account</NavLink>
          </nav>
          <div className="user">
            {user?.name && <span className="user-name">{user.name}</span>}
            {user?.isAdmin && <span className="role-tag">Admin</span>}
            <button type="button" className="btn btn-ghost btn-sm" onClick={logout}>
              Log out
            </button>
          </div>
        </div>
      </header>
      <main className="container">
        <Outlet />
      </main>
    </>
  );
}
