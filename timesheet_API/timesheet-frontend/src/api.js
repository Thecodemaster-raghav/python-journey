/**
 * api.js — the ONLY place that talks to the backend.
 *
 * - Base URL comes from VITE_API_URL (never hardcoded).
 * - `request()` is the central wrapper: it attaches the bearer token,
 *   parses JSON, normalises errors, and handles 401/403 in one spot.
 * - `api` lists every endpoint the app uses.
 */

const BASE_URL = (import.meta.env.VITE_API_URL || '').replace(/\/+$/, '');
const TOKEN_KEY = 'timesheet.token';

/* ---------- Token storage ---------- */

export const tokenStore = {
  get() {
    try { return localStorage.getItem(TOKEN_KEY); } catch { return null; }
  },
  set(token) {
    try { localStorage.setItem(TOKEN_KEY, token); } catch { /* storage unavailable */ }
  },
  clear() {
    try { localStorage.removeItem(TOKEN_KEY); } catch { /* storage unavailable */ }
  },
};

/* ---------- 401/403 hook (set by AuthProvider) ---------- */

let unauthorizedHandler = null;
export function setUnauthorizedHandler(fn) {
  unauthorizedHandler = fn;
}

/* ---------- Errors ---------- */

export class ApiError extends Error {
  constructor(message, status = 0, body = null) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.body = body;
  }
}

// FastAPI sends { detail: "..." } or { detail: [{ msg, loc }, ...] } for 422s.
function messageFrom(body, status) {
  const detail = body && typeof body === 'object' ? body.detail : null;
  if (typeof detail === 'string') return detail;
  if (Array.isArray(detail) && detail.length) {
    return detail.map((d) => d?.msg).filter(Boolean).join(' ');
  }
  if (typeof body === 'string' && body.trim()) return body;
  return `Request failed (${status}).`;
}

/* ---------- Central request wrapper ---------- */

async function request(path, { method = 'GET', body, query, auth = true } = {}) {
  if (!BASE_URL) {
    throw new ApiError('VITE_API_URL is not set. Add it to your .env file and restart the dev server.');
  }

  const url = new URL(BASE_URL + path);
  if (query) {
    Object.entries(query).forEach(([key, value]) => {
      if (value !== undefined && value !== null && value !== '') url.searchParams.set(key, value);
    });
  }

  const headers = { Accept: 'application/json' };
  if (body !== undefined) headers['Content-Type'] = 'application/json';
  if (auth) {
    const token = tokenStore.get();
    if (token) headers.Authorization = `Bearer ${token}`;
  }

  let res;
  try {
    res = await fetch(url, {
      method,
      headers,
      body: body !== undefined ? JSON.stringify(body) : undefined,
    });
  } catch {
    throw new ApiError("Can't reach the server. Check your connection and try again.");
  }

  // Protected call rejected → session is over. Public calls (login/register)
  // skip this so a wrong password shows an error instead of a redirect.
  if (auth && (res.status === 401 || res.status === 403)) {
    tokenStore.clear();
    unauthorizedHandler?.();
    throw new ApiError('Your session has ended. Log in again.', res.status);
  }

  const text = await res.text();
  let data = null;
  if (text) {
    try { data = JSON.parse(text); } catch { data = text; }
  }

  if (!res.ok) throw new ApiError(messageFrom(data, res.status), res.status, data);
  return data;
}

/* ---------- Endpoints ---------- */

const enc = encodeURIComponent;

export const api = {
  register: ({ name, username, password }) =>
    request('/register', { method: 'POST', body: { name, username, password }, auth: false }),

  login: ({ username, password }) =>
    request('/login', { method: 'POST', body: { username, password }, auth: false }),

  clockIn: () =>
    request('/shifts', { method: 'POST' }),

  clockOut: (shiftId) =>
    request(`/shifts/${enc(shiftId)}/clock_out`, { method: 'PUT' }),

  totalHours: (workerId) =>
    request(`/workers/${enc(workerId)}/hours`),

  breakdown: (workerId, { period, start, end }) =>
    request(`/workers/${enc(workerId)}/breakdown`, { query: { period, start, end } }),

  deleteAccount: () =>
    request('/account', { method: 'DELETE' }),

  allShifts: () =>
    request('/admin'),

  // changes: { clock_in?: ISO string, clock_out?: ISO string }
  correctShift: (shiftId, changes) =>
    request(`/admin/${enc(shiftId)}`, { method: 'PATCH', body: changes }),
};
