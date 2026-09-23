# Timesheet — React frontend

Vite + React 18 + React Router. No UI library; styles live in `src/index.css`.
Date pickers are the browser's native `<input type="date">` and `<input type="datetime-local">`.

## Run it

```bash
npm install
cp .env.example .env      # then set VITE_API_URL to your FastAPI base URL
npm run dev               # http://localhost:5173
```

Restart `npm run dev` after changing `.env` — Vite reads it at startup.

## Where things live

```
src/
  api.js                 ← every backend call + the central request wrapper
  auth/
    claims.js            ← JWT decoding + readIdentity()  (adjust claim names here)
    AuthContext.jsx      ← token state, login/logout, 401/403 → /login
    guards.jsx           ← RequireAuth, RequireAdmin, PublicOnly
  hooks/useRequest.js    ← loading / error / data for a request
  lib/datetime.js        ← ISO-with-offset out, human-readable in
  lib/openShift.js       ← remembers the open shift id on this device
  components/            ← Layout, ShiftCard, MyHours, ConfirmDialog, ui bits
  pages/                 ← Login, Register, Dashboard, Admin, Account
```

## Backend assumptions to check

1. **CORS.** The browser blocks calls from `localhost:5173` unless FastAPI adds
   `CORSMiddleware` allowing that origin and the `Authorization` header.
2. **JWT claims.** `/login` returns only the token, so the worker id and admin flag
   are read from the token payload. `readIdentity()` looks for
   `worker_id` → `id` → `sub` for the id, and `is_admin: true` / `admin: true` /
   `role: "admin"` for admin. Change it if your token differs.
3. **`POST /shifts` response.** The clock-out button needs the new shift's id, read
   from `shift_id` or `id` in the response (and `clock_in` if present).
4. **`POST /login` body.** Sent as JSON `{ username, password }`. If the route uses
   `OAuth2PasswordRequestForm`, it expects form data instead — change `api.login`.
5. **`GET /admin` shape.** Expected: an array of shifts with `shift_id`/`id`,
   `worker_id`, `clock_in`, `clock_out` (and optionally `worker_name`/`name`).
