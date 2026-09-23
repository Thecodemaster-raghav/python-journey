import { useState } from 'react';
import { api } from '../api.js';
import { useAuth } from '../auth/AuthContext.jsx';
import ConfirmDialog from '../components/ConfirmDialog.jsx';
import { openShiftStore } from '../lib/openShift.js';

export default function AccountPage() {
  const { user, endSession } = useAuth();
  const [confirming, setConfirming] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');

  async function handleDelete() {
    setBusy(true);
    setError('');
    try {
      await api.deleteAccount();
      openShiftStore.clear(user.workerId);
      endSession('deleted');
    } catch (e) {
      setError(e.message);
      setBusy(false);
    }
  }

  return (
    <div className="page">
      <header className="page-head">
        <h1>Account</h1>
      </header>

      <section className="panel" aria-labelledby="profile-title">
        <h2 id="profile-title">Profile</h2>
        <dl className="kv">
          <dt>Name</dt><dd>{user?.name ?? '—'}</dd>
          {user?.username && (<><dt>Username</dt><dd>{user.username}</dd></>)}
          <dt>Worker ID</dt><dd className="num">{user?.workerId ?? '—'}</dd>
          <dt>Role</dt><dd>{user?.isAdmin ? 'Admin' : 'Worker'}</dd>
        </dl>
      </section>

      <section className="panel danger-zone" aria-labelledby="delete-title">
        <div>
          <h2 id="delete-title">Delete account</h2>
          <p className="muted">
            Permanently removes your account and logs you out. This can't be undone.
          </p>
        </div>
        <div>
          <button type="button" className="btn btn-danger" onClick={() => { setError(''); setConfirming(true); }}>
            Delete my account
          </button>
        </div>
      </section>

      <ConfirmDialog
        open={confirming}
        title="Are you sure?"
        confirmLabel="Yes, delete my account"
        busyLabel="Deleting…"
        busy={busy}
        error={error}
        onConfirm={handleDelete}
        onCancel={() => setConfirming(false)}
      >
        Your account and access to your timesheet will be deleted permanently. You'll need to
        register again to use Timesheet.
      </ConfirmDialog>
    </div>
  );
}
