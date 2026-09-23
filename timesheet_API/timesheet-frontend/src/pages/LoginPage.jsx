import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useAuth } from '../auth/AuthContext.jsx';
import { AuthShell } from '../components/ui.jsx';

const NOTICES = {
  expired: 'Your session ended. Log in again to continue.',
  deleted: 'Your account has been deleted.',
  registered: 'Account created. Log in with your new username.',
};

export default function LoginPage() {
  const { login } = useAuth();
  const location = useLocation();
  const [form, setForm] = useState({ username: '', password: '' });
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');

  const notice = NOTICES[location.state?.reason];
  const update = (key) => (e) => setForm((f) => ({ ...f, [key]: e.target.value }));

  async function handleSubmit(e) {
    e.preventDefault();
    setBusy(true);
    setError('');
    try {
      await login(form.username.trim(), form.password);
      // PublicOnly redirects once the token is stored.
    } catch {
      // Deliberately generic: don't reveal whether the username exists.
      setError("Couldn't log you in. Check your username and password and try again.");
      setBusy(false);
    }
  }

  return (
    <AuthShell
      title="Log in"
      subtitle="Clock in, clock out, and see your hours."
      footer={<>New here? <Link to="/register">Create an account</Link></>}
    >
      {notice && <p className="form-notice" role="status">{notice}</p>}
      <form className="form" onSubmit={handleSubmit} noValidate>
        <div className="field">
          <label htmlFor="username">Username</label>
          <input
            id="username" className="input" autoComplete="username" required autoFocus
            value={form.username} onChange={update('username')}
          />
        </div>
        <div className="field">
          <label htmlFor="password">Password</label>
          <input
            id="password" type="password" className="input" autoComplete="current-password" required
            value={form.password} onChange={update('password')}
          />
        </div>
        {error && <p className="form-error" role="alert">{error}</p>}
        <button
          type="submit" className="btn btn-primary btn-block"
          disabled={busy || !form.username.trim() || !form.password}
        >
          {busy ? 'Logging in…' : 'Log in'}
        </button>
      </form>
    </AuthShell>
  );
}
