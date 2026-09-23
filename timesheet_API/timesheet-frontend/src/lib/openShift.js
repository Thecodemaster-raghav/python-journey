/**
 * Remembers the open shift ({ id, clockIn }) on this device so the worker
 * can clock out after a refresh. Keyed per worker.
 * (The API has no "get my open shift" endpoint for non-admins.)
 */
const key = (workerId) => `timesheet.openShift.${workerId}`;

export const openShiftStore = {
  load(workerId) {
    try {
      const raw = localStorage.getItem(key(workerId));
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  },
  save(workerId, shift) {
    try { localStorage.setItem(key(workerId), JSON.stringify(shift)); } catch { /* ignore */ }
  },
  clear(workerId) {
    try { localStorage.removeItem(key(workerId)); } catch { /* ignore */ }
  },
};
