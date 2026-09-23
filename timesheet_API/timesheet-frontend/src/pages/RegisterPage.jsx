import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { api } from '../api.js';
import { AuthShell } from '../components/ui.jsx';

export default function RegisterPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: '', username: '', password: '' });
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');

  const update = (key) => (e) => setForm((f) => ({ ...f, [key]: e.target.value }));
  const canSubmit = form.name.trim() && form.username.trim() && form.password;

  async function handleSubmit(e) {
    e.preventDefault();
    if (!canSubmit) return;
    setBusy(true);
    setError('');
    try {
      await api.register({
        name: form.name.trim(),
        username: form.username.trim(),
        password: form.password,
      });
      navigate('/login', { replace: true, state: { reason: 'registered' } });
    } catch (err) {
      setError(err.message || "Couldn't create the account. Try again.");
      setBusy(false);
    }
  }

  return (
    <AuthShell
      title="Create an account"
      subtitle="You'll use your username to log in."
      footer={<>Already have an account? <Link to="/login">Log in</Link></>}
    >
      <form className="form" onSubmit={handleSubmit} noValidate>
        <div className="field">
          <label htmlFor="name">Full name</label>
          <input id="name" className="input" autoComplete="name" required autoFocus
            value={form.name} onChange={update('name')} />
        </div>
        <div className="field">
          <label htmlFor="username">Username</label>
          <input id="username" className="input" autoComplete="username" required
            value={form.username} onChange={update('username')} />
        </div>
        <div className="field">
          <label htmlFor="password">Password</label>
          <input id="password" type="password" className="input" autoComplete="new-password" required
            value={form.password} onChange={update('password')} />
        </div>
        {error && <p className="form-error" role="alert">{error}</p>}
        <button type="submit" className="btn btn-primary btn-block" disabled={busy || !canSubmit}>
          {busy ? 'Creating account…' : 'Create account'}
        </button>
      </form>
    </AuthShell>
  );
}
