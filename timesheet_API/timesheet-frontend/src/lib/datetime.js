/**
 * Date helpers.
 * Outgoing datetimes: ISO 8601 with the local UTC offset, e.g. 2026-09-22T17:00:00-06:00
 * Incoming datetimes: ISO strings, formatted for humans before display.
 */

const pad = (n) => String(n).padStart(2, '0');

export function parseIso(value) {
  if (!value) return null;
  const d = new Date(value);
  return Number.isNaN(d.getTime()) ? null : d;
}

export function toIsoWithOffset(date) {
  const offset = -date.getTimezoneOffset();
  const sign = offset >= 0 ? '+' : '-';
  const abs = Math.abs(offset);
  return (
    `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}` +
    `T${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}` +
    `${sign}${pad(Math.floor(abs / 60))}:${pad(abs % 60)}`
  );
}

/** YYYY-MM-DD in local time — the value format of <input type="date">. */
export function toDateInputValue(date) {
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
}

/** ISO string → value for <input type="datetime-local"> (YYYY-MM-DDTHH:mm). */
export function toLocalInputValue(iso) {
  const d = parseIso(iso);
  if (!d) return '';
  return `${toDateInputValue(d)}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

/** <input type="datetime-local"> value → ISO 8601 with offset. */
export function fromLocalInputValue(value) {
  return toIsoWithOffset(new Date(value)); // no zone in value → parsed as local time
}

export function formatDateTime(iso) {
  const d = parseIso(iso);
  if (!d) return '—';
  return d.toLocaleString(undefined, {
    weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit',
  });
}

export function formatTime(iso) {
  const d = parseIso(iso);
  return d ? d.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' }) : '—';
}

/** Milliseconds → H:MM:SS */
export function formatDuration(ms) {
  const total = Math.max(0, Math.floor(ms / 1000));
  const h = Math.floor(total / 3600);
  const m = Math.floor((total % 3600) / 60);
  const s = total % 60;
  return `${h}:${pad(m)}:${pad(s)}`;
}

export function hoursBetween(startIso, endIso) {
  const a = parseIso(startIso);
  const b = parseIso(endIso);
  if (!a || !b) return null;
  return (b - a) / 3_600_000;
}

export function formatHours(value) {
  const n = Number(value);
  if (value === null || value === undefined || !Number.isFinite(n)) return '—';
  return `${n.toLocaleString(undefined, { maximumFractionDigits: 2 })} h`;
}

/** period_start ("2026-09-14" or full ISO) → "Week of Sep 14, 2026" / "September 2026" */
export function formatPeriodLabel(value, period) {
  const match = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(value || ''));
  if (!match) return String(value ?? '—');
  const d = new Date(Number(match[1]), Number(match[2]) - 1, Number(match[3]));
  if (period === 'monthly') {
    return d.toLocaleDateString(undefined, { month: 'long', year: 'numeric' });
  }
  return `Week of ${d.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })}`;
}
