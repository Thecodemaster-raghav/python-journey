import { Link } from 'react-router-dom';

export function BrandMark() {
  return (
    <svg className="brand-mark" viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="16" r="13" fill="none" stroke="currentColor" strokeWidth="3" />
      <path d="M16 9v7l5 3" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" />
    </svg>
  );
}

export function Brand() {
  return (
    <Link to="/" className="brand">
      <BrandMark />
      <span>Timesheet</span>
    </Link>
  );
}

export function Spinner({ label = 'Loading…' }) {
  return (
    <div className="loading" role="status">
      <span className="spinner" aria-hidden="true" />
      <span>{label}</span>
    </div>
  );
}

export function ErrorNote({ error, onRetry }) {
  if (!error) return null;
  const message = typeof error === 'string' ? error : error.message;
  return (
    <div className="form-error" role="alert">
      <span>{message}</span>
      {onRetry && (
        <button type="button" className="btn-link" onClick={onRetry}>Try again</button>
      )}
    </div>
  );
}

export function AuthShell({ title, subtitle, children, footer }) {
  return (
    <main className="auth">
      <div className="auth-card">
        <Brand />
        <div className="auth-head">
          <h1>{title}</h1>
          {subtitle && <p>{subtitle}</p>}
        </div>
        {children}
        {footer && <p className="auth-foot">{footer}</p>}
      </div>
    </main>
  );
}
