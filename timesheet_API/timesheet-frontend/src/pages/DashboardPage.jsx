import { useState } from 'react';
import { useAuth } from '../auth/AuthContext.jsx';
import MyHours from '../components/MyHours.jsx';
import ShiftCard from '../components/ShiftCard.jsx';

function greeting() {
  const h = new Date().getHours();
  if (h < 12) return 'Good morning';
  if (h < 18) return 'Good afternoon';
  return 'Good evening';
}

export default function DashboardPage() {
  const { user } = useAuth();
  const [hoursVersion, setHoursVersion] = useState(0);
  const firstName = user?.name ? String(user.name).split(' ')[0] : null;

  if (user?.workerId === null || user?.workerId === undefined) {
    return (
      <div className="page">
        <p className="form-error" role="alert">
          Your login token doesn't include a worker id, so your hours can't be loaded.
          Update readIdentity() in src/auth/claims.js to match your token's claims.
        </p>
      </div>
    );
  }

  return (
    <div className="page">
      <header className="page-head">
        <h1>{firstName ? `${greeting()}, ${firstName}` : greeting()}</h1>
        <p>{new Date().toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric' })}</p>
      </header>

      <div className="dash-grid">
        <ShiftCard workerId={user.workerId} onShiftClosed={() => setHoursVersion((v) => v + 1)} />
        <MyHours workerId={user.workerId} refreshKey={hoursVersion} />
      </div>
    </div>
  );
}
