import { useEffect, useRef } from 'react';

/** Modal confirm built on the native <dialog> (focus trap + Escape for free). */
export default function ConfirmDialog({
  open, title, children, confirmLabel, busyLabel, busy, error, onConfirm, onCancel,
}) {
  const dialogRef = useRef(null);
  const cancelRef = useRef(null);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;
    if (open && !dialog.open) {
      dialog.showModal();
      cancelRef.current?.focus(); // safe default for destructive actions
    } else if (!open && dialog.open) {
      dialog.close();
    }
  }, [open]);

  return (
    <dialog
      ref={dialogRef}
      className="dialog"
      aria-labelledby="confirm-title"
      onCancel={(e) => {
        e.preventDefault();
        if (!busy) onCancel();
      }}
    >
      <h2 id="confirm-title">{title}</h2>
      <div className="dialog-body">{children}</div>
      {error && <p className="form-error" role="alert">{error}</p>}
      <div className="dialog-actions">
        <button ref={cancelRef} type="button" className="btn btn-ghost" onClick={onCancel} disabled={busy}>
          Cancel
        </button>
        <button type="button" className="btn btn-danger" onClick={onConfirm} disabled={busy}>
          {busy ? busyLabel : confirmLabel}
        </button>
      </div>
    </dialog>
  );
}
