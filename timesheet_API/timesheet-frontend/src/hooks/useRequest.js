import { useCallback, useEffect, useState } from 'react';

/**
 * Runs an async request when `deps` change and tracks loading/error/data.
 * Keeps the previous data visible while reloading so the UI doesn't flash.
 */
export function useRequest(fn, deps, { enabled = true } = {}) {
  const [state, setState] = useState({ data: null, error: null, loading: enabled });
  const [nonce, setNonce] = useState(0);

  useEffect(() => {
    if (!enabled) {
      setState((s) => ({ ...s, loading: false }));
      return undefined;
    }
    let cancelled = false;
    setState((s) => ({ ...s, loading: true, error: null }));
    fn().then(
      (data) => { if (!cancelled) setState({ data, error: null, loading: false }); },
      (error) => { if (!cancelled) setState({ data: null, error, loading: false }); }
    );
    return () => { cancelled = true; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [...deps, enabled, nonce]);

  const reload = useCallback(() => setNonce((n) => n + 1), []);
  return { ...state, reload };
}

/** Current time, ticking every second while `active`. */
export function useNow(active) {
  const [now, setNow] = useState(() => Date.now());
  useEffect(() => {
    if (!active) return undefined;
    setNow(Date.now());
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);
  }, [active]);
  return now;
}
