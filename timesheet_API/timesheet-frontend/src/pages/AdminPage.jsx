import { useEffect, useMemo, useState } from 'react';
import { api } from '../api.js';
import { useRequest } from '../hooks/useRequest.js';
import { ErrorNote, Spinner } from '../components/ui.jsx';
import {
  formatDateTime, formatHours, fromLocalInputValue, hoursBetween, parseIso, toLocalInputValue,
} from '../lib/datetime.js';

function normalise(data) {
  const list = Array.isArray(data) ? data : data?.shifts ?? [];
  return list
    .map((s) => ({
      id: s.shift_id ?? s.id,
      workerId: s.worker_id,
      worker: s.worker_name ?? s.name ?? s.username ?? null,
      clockIn: s.clock_in,
      clockOut: s.clock_out,
    }))
    .sort((a, b) => (parseIso(b.clockIn)?.getTime() ?? 0) - (parseIso(a.clockIn)?.getTime() ?? 0));
}

export default function AdminPage() {
  const shifts = useRequest(() => api.allShifts(), []);
  const [editingId, setEditingId] = useState(null);
  const [search, setSearch] = useState('');
  const [openOnly, setOpenOnly] = useState(false);

  const rows = useMemo(() => normalise(shifts.data), [shifts.data]);
  const visible = rows.filter((r) => {
    if (openOnly && r.clockOut) return false;
    const q = search.trim().toLowerCase();
    if (!q) return true;
    return String(r.worker ?? '').toLowerCase().includes(q) || String(r.workerId ?? '') === q;
  });

  return (
    <div className="page">
      <header className="page-head">
        <h1>All shifts</h1>
        <p>Correct a clock-in or clock-out time when someone forgets to punch.</p>
      </header>

      <section className="panel" aria-label="Shifts">
        <div className="toolbar">
          <div className="field toolbar-search">
            <label htmlFor="shift-search">Find a worker</label>
            <input
              id="shift-search" type="search" className="input" placeholder="Name or worker ID"
              value={search} onChange={(e) => setSearch(e.target.value)}
            />
          </div>
          <label className="check">
            <input type="checkbox" checked={openOnly} onChange={(e) => setOpenOnly(e.target.checked)} />
            Open shifts only
          </label>
          <button type="button" className="btn btn-ghost" onClick={shifts.reload} disabled={shifts.loading}>
            {shifts.loading ? 'Refreshing…' : 'Refresh'}
          </button>
        </div>

        <ErrorNote error={shifts.error} onRetry={shifts.reload} />
        {shifts.loading && rows.length === 0 && <Spinner label="Loading shifts…" />}

        {!shifts.loading && !shifts.error && visible.length === 0 && (
          <p className="empty">
            {rows.length === 0 ? 'No shifts recorded yet.' : 'No shifts match these filters.'}
          </p>
        )}

        {visible.length > 0 && (
          <>
            <p className="hint">Showing {visible.length} of {rows.length} shifts</p>
            <div className="table-wrap">
              <table className="shifts">
                <thead>
                  <tr>
                    <th scope="col">Shift</th>
                    <th scope="col">Worker</th>
                    <th scope="col">Clock in</th>
                    <th scope="col">Clock out</th>
                    <th scope="col">Hours</th>
                    <th scope="col"><span className="sr-only">Actions</span></th>
                  </tr>
                </thead>
                <tbody>
                  {visible.map((shift) => (
                    <ShiftRow
                      key={shift.id}
                      shift={shift}
                      isEditing={editingId === shift.id}
                      locked={editingId !== null && editingId !== shift.id}
                      onEdit={() => setEditingId(shift.id)}
                      onCancel={() => setEditingId(null)}
                      onSaved={() => { setEditingId(null); shifts.reload(); }}
                    />
                  ))}
                </tbody>
              </table>
            </div>
          </>
        )}
      </section>
    </div>
  );
}

function ShiftRow({ shift, isEditing, locked, onEdit, onCancel, onSaved }) {
  const initial = { clockIn: toLocalInputValue(shift.clockIn), clockOut: toLocalInputValue(shift.clockOut) };
  const [draft, setDraft] = useState(initial);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (isEditing) {
      setDraft({ clockIn: toLocalInputValue(shift.clockIn), clockOut: toLocalInputValue(shift.clockOut) });
      setError('');
    }
  }, [isEditing, shift.clockIn, shift.clockOut]);

  async function save() {
    const changes = {};
    if (draft.clockIn !== initial.clockIn) {
      if (!draft.clockIn) return setError('Clock in needs a date and time.');
      changes.clock_in = fromLocalInputValue(draft.clockIn);
    }
    if (draft.clockOut !== initial.clockOut) {
      if (!draft.clockOut) return setError("Clock out can't be cleared here. Pick a date and time.");
      changes.clock_out = fromLocalInputValue(draft.clockOut);
    }
    if (Object.keys(changes).length === 0) return onCancel();
    if (draft.clockIn && draft.clockOut && new Date(draft.clockOut) <= new Date(draft.clockIn)) {
      return setError('Clock out must be after clock in.');
    }

    setSaving(true);
    setError('');
    try {
      await api.correctShift(shift.id, changes); // sends only the fields that changed
      onSaved();
    } catch (e) {
      setError(e.message);
    } finally {
      setSaving(false);
    }
    return undefined;
  }

  function handleKeyDown(e) {
    if (e.key === 'Escape' && !saving) onCancel();
    if (e.key === 'Enter') { e.preventDefault(); save(); }
  }

  const hours = hoursBetween(shift.clockIn, shift.clockOut);

  return (
    <>
      <tr className={isEditing ? 'is-editing' : undefined}>
        <td data-label="Shift" className="num">#{shift.id}</td>
        <td data-label="Worker">
          {shift.worker ?? <span className="muted">Worker #{shift.workerId}</span>}
        </td>
        <td data-label="Clock in">
          {isEditing ? (
            <input
              type="datetime-local" className="input input-compact" aria-label={`Clock in for shift ${shift.id}`}
              value={draft.clockIn} max={draft.clockOut || undefined}
              onChange={(e) => setDraft((d) => ({ ...d, clockIn: e.target.value }))}
              onKeyDown={handleKeyDown} autoFocus
            />
          ) : formatDateTime(shift.clockIn)}
        </td>
        <td data-label="Clock out">
          {isEditing ? (
            <input
              type="datetime-local" className="input input-compact" aria-label={`Clock out for shift ${shift.id}`}
              value={draft.clockOut} min={draft.clockIn || undefined}
              onChange={(e) => setDraft((d) => ({ ...d, clockOut: e.target.value }))}
              onKeyDown={handleKeyDown}
            />
          ) : shift.clockOut ? formatDateTime(shift.clockOut) : <span className="open-tag">Open</span>}
        </td>
        <td data-label="Hours" className="num">{hours === null ? '—' : formatHours(hours)}</td>
        <td className="row-actions-cell">
          <div className="row-actions">
            {isEditing ? (
              <>
                <button type="button" className="btn btn-primary btn-sm" onClick={save} disabled={saving}>
                  {saving ? 'Saving…' : 'Save'}
                </button>
                <button type="button" className="btn btn-ghost btn-sm" onClick={onCancel} disabled={saving}>
                  Cancel
                </button>
              </>
            ) : (
              <button type="button" className="btn btn-ghost btn-sm" onClick={onEdit} disabled={locked}>
                Edit times
              </button>
            )}
          </div>
        </td>
      </tr>
      {isEditing && error && (
        <tr className="row-error">
          <td colSpan={6}><p className="form-error" role="alert">{error}</p></td>
        </tr>
      )}
    </>
  );
}
