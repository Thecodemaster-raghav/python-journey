import { useState } from 'react';
import { api } from '../api.js';
import { useNow } from '../hooks/useRequest.js';
import { openShiftStore } from '../lib/openShift.js';
import {
  formatDateTime, formatDuration, formatHours, formatTime,
  hoursBetween, parseIso, toIsoWithOffset,
} from '../lib/datetime.js';

export default function ShiftCard({ workerId, onShiftClosed }) {
  const [openShift, setOpenShift] = useState(() => openShiftStore.load(workerId));
  const [lastShift, setLastShift] = useState(null);
  const [busy, setBusy] = useState(null); // 'in' | 'out' | null
  const [error, setError] = useState('');
  const now = useNow(Boolean(openShift));

  async function handleClockIn() {
    setBusy('in');
    setError('');
    try {
      const data = await api.clockIn();
      const id = data?.shift_id ?? data?.id;
      if (id === undefined || id === null) {
        throw new Error("Clocked in, but the server didn't return a shift id, so this page can't clock you out.");
      }
      const shift = { id, clockIn: data?.clock_in ?? toIsoWithOffset(new Date()) };
      openShiftStore.save(workerId, shift);
      setOpenShift(shift);
      setLastShift(null);
    } catch (e) {
      setError(e.message);
    } finally {
      setBusy(null);
    }
  }

  async function handleClockOut() {
    setBusy('out');
    setError('');
    try {
      const data = await api.clockOut(openShift.id);
      setLastShift({
        clockIn: data?.clock_in ?? openShift.clockIn,
        clockOut: data?.clock_out ?? toIsoWithOffset(new Date()),
      });
      openShiftStore.clear(workerId);
      setOpenShift(null);
      onShiftClosed?.();
    } catch (e) {
      setError(e.message);
    } finally {
      setBusy(null);
    }
  }

  // Escape hatch if the shift was closed elsewhere (e.g. an admin correction).
  function forgetShift() {
    openShiftStore.clear(workerId);
    setOpenShift(null);
    setError('');
  }

  const isOn = Boolean(openShift);
  const startedAt = isOn ? parseIso(openShift.clockIn) : null;

  return (
    <section className={`timecard${isOn ? ' is-on' : ''}`} aria-labelledby="timecard-title">
      <div className="timecard-head">
        <h2 id="timecard-title">Time card</h2>
        <span className="status-pill">{isOn ? 'On shift' : 'Off the clock'}</span>
      </div>

      <div className="timer-row">
        <p className={`timer${isOn ? '' : ' timer-idle'}`}>
          {isOn && startedAt ? formatDuration(now - startedAt.getTime()) : '0:00:00'}
        </p>
        {isOn && (
          <div className="stamp" aria-hidden="true">
            <span className="stamp-word">In</span>
            <span className="stamp-time">{formatTime(openShift.clockIn)}</span>
          </div>
        )}
      </div>

      <p className="timecard-meta">
        {isOn && `Clocked in ${formatDateTime(openShift.clockIn)}`}
        {!isOn && lastShift &&
          `Last shift: ${formatHours(hoursBetween(lastShift.clockIn, lastShift.clockOut))}, ${formatTime(lastShift.clockIn)} to ${formatTime(lastShift.clockOut)}`}
        {!isOn && !lastShift && 'Clock in when your shift starts.'}
      </p>

      {error && (
        <div className="form-error" role="alert">
          <span>{error}</span>
          {isOn && (
            <button type="button" className="btn-link" onClick={forgetShift}>
              Stop tracking this shift on this device
            </button>
          )}
        </div>
      )}

      <div className="timecard-actions">
        <button
          type="button"
          className="btn btn-primary btn-lg"
          onClick={handleClockIn}
          disabled={isOn || Boolean(busy)}
        >
          {busy === 'in' ? 'Clocking in…' : 'Clock in'}
        </button>
        <button
          type="button"
          className="btn btn-shift btn-lg"
          onClick={handleClockOut}
          disabled={!isOn || Boolean(busy)}
        >
          {busy === 'out' ? 'Clocking out…' : 'Clock out'}
        </button>
      </div>
    </section>
  );
}
