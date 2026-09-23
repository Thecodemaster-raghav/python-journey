/**
 * The login response only carries the token, so the app reads identity
 * (worker id, display name, admin flag) from the JWT payload.
 *
 * Decoding here is for UX only — it is NOT verification. The backend
 * remains the authority on who can do what.
 *
 * ⚙️  If your backend uses different claim names, change readIdentity().
 */

export function decodeJwt(token) {
  try {
    const part = token.split('.')[1];
    const b64 = part.replace(/-/g, '+').replace(/_/g, '/');
    const padded = b64 + '='.repeat((4 - (b64.length % 4)) % 4);
    const bytes = Uint8Array.from(atob(padded), (c) => c.charCodeAt(0));
    return JSON.parse(new TextDecoder().decode(bytes));
  } catch {
    return null;
  }
}

export function isExpired(claims) {
  return Boolean(claims?.exp && claims.exp * 1000 <= Date.now());
}

export function readIdentity(claims) {
  if (!claims) return null;
  return {
    workerId: claims.worker_id ?? claims.id ?? claims.sub ?? null,
    name: claims.name ?? claims.username ?? (typeof claims.sub === 'string' ? claims.sub : null),
    username: claims.username ?? null,
    isAdmin: claims.is_admin === true || claims.admin === true || claims.role === 'admin',
  };
}
