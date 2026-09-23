import { useMemo, useState } from 'react';
import { api } from '../api.js';
import { useRequest } from '../hooks/useRequest.js';
import { formatHours, formatPeriodLabel, toDateInputValue } from '../lib/datetime.js';
import { ErrorNote, Spinner } from './ui.jsx';

const PRESETS = [
  { id: '4w', label: 'Last 4 weeks' },
  { id: '12w', label: 'Last 12 weeks' },
  { id: '6m', label: 'Last 6 months' },
  { id: 'ytd', label: 'This year' },
];

function rangeFor(preset) {
  const end = new Date();
  const start = new Date(end);
  if (preset === '4w') start.setDate(start.getDate() - 27);
  if (preset === '12w') start.setDate(start.getDate() - 83);
  if (preset === '6m') { start.setMonth(start.getMonth() - 5); start.setDate(1); }
  if (preset === 'ytd') start.setMonth(0, 1);
  return { start: toDateInputValue(start), end: toDateInputValue(end) };
}

export default function MyHours({ workerId, refreshKey }) {
  const [period, setPeriod] = useState('weekly');
  const [range, setRange] = useState(() => rangeFor('12w'));

  const rangeError =
    !range.start || !range.end ? 'Pick both a start and an end date.'
      : range.start > range.end ? 'The start date must be on or before the end date.'
        : '';

  const total = useRequest(() => api.totalHours(workerId), [workerId, refreshKey]);
  const breakdown = useRequest(
    () => api.breakdown(workerId, { period, start: range.start, end: range.end }),
    [workerId, period, range.start, range.end, refreshKey],
    { enabled: !rangeError }
  );

  const rows = useMemo(() => {
    const list = Array.isArray(breakdown.data) ? breakdown.data : [];
    return list
      .map((r) => ({ start: r.period_start, hours: Number(r.total_hours) || 0 }))
      .sort((a, b) => String(a.start).localeCompare(String(b.start)));
  }, [breakdown.data]);

  const maxHours = Math.max(1, ...rows.map((r) => r.hours));
  const rangeTotal = rows.reduce((sum, r) => sum + r.hours, 0);

  return (
    <section className="panel" aria-labelledby="hours-title">
      <div className="panel-head">
        <h2 id="hours-title">My hours</h2>
        <div className="total" aria-live="polite">
          {total.loading && !total.data ? (
            <Spinner label="Loading total…" />
          ) : total.error ? null : (
            <>
              <span className="total-value">{formatHours(total.data?.total_hours ?? 0)}</span>
              <span className="total-unit">all time</span>
            </>
          )}
        </div>
      </div>
      <ErrorNote error={total.error} onRetry={total.reload} />

      <div className="controls">
        <div className="segmented" role="group" aria-label="Group by">
          {['weekly', 'monthly'].map((p) => (
            <button key={p} type="button" aria-pressed={period === p} onClick={() => setPeriod(p)}>
              {p === 'weekly' ? 'Weekly' : 'Monthly'}
            </button>
          ))}
        </div>
        <div className="date-range">
          <div className="field">
            <label htmlFor="range-start">From</label>
            <input
              id="range-start" type="date" className="input"
              value={range.start} max={range.end || undefined}
              onChange={(e) => setRange((r) => ({ ...r, start: e.target.value }))}
            />
          </div>
          <div className="field">
            <label htmlFor="range-end">To</label>
            <input
              id="range-end" type="date" className="input"
              value={range.end} min={range.start || undefined}
              onChange={(e) => setRange((r) => ({ ...r, end: e.target.value }))}
            />
          </div>
        </div>
      </div>
      <div className="presets" role="group" aria-label="Quick ranges">
        {PRESETS.map((p) => (
          <button key={p.id} type="button" className="chip" onClick={() => setRange(rangeFor(p.id))}>
            {p.label}
          </button>
        ))}
      </div>

      {rangeError && <p className="form-error" role="alert">{rangeError}</p>}
      {!rangeError && <ErrorNote error={breakdown.error} onRetry={breakdown.reload} />}

      {!rangeError && breakdown.loading && rows.length === 0 && <Spinner label="Loading breakdown…" />}

      {!rangeError && !breakdown.loading && !breakdown.error && rows.length === 0 && (
        <p className="empty">No hours logged in this range. Try a wider date range.</p>
      )}

      {!rangeError && rows.length > 0 && (
        <>
          <ul className={`bars${breakdown.loading ? ' is-stale' : ''}`}>
            {rows.map((r) => (
              <li key={r.start} className="bar-row">
                <span className="bar-label">{formatPeriodLabel(r.start, period)}</span>
                <span className="bar-track" aria-hidden="true">
                  <span className="bar-fill" style={{ width: `${(r.hours / maxHours) * 100}%` }} />
                </span>
                <span className="bar-value">{formatHours(r.hours)}</span>
              </li>
            ))}
          </ul>
          <p className="hint">{formatHours(rangeTotal)} in this range</p>
        </>
      )}
    </section>
  );
}
