# all admin read and write routes
from fastapi import APIRouter, HTTPException, Depends
from dependencies import get_conn, verify_tokens
from models import UpdateEntry

router = APIRouter()

@router.get("/admin")
async def admin_shifts(conn_admin=Depends(get_conn), tokens=Depends(verify_tokens)):
    async with conn_admin.cursor() as cur:
        await cur.execute("SELECT role FROM workers WHERE worker_id=%s", (tokens,))
        caller = await cur.fetchone()
        if caller is None:
            raise HTTPException(status_code=404, detail="Invalid Entry")
        if caller["role"] != "admin":
            raise HTTPException(status_code=403, detail="Access Forbidden")
        await cur.execute("SELECT * FROM shifts")
        rows = await cur.fetchall()
        return rows 

# admin route for updating or changing the clock-in clock-out times for workers
# query the callers role; 403 if not admin
@router.patch("/admin/{shift_id}")
async def update_entry(entry: UpdateEntry, shift_id: int, conn=Depends(get_conn), tokens=Depends(verify_tokens)):
    async with conn.cursor() as cur:
        await cur.execute("SELECT role FROM workers WHERE worker_id=%s", (tokens,))
        rows = await cur.fetchone()
        if rows is None:
            raise HTTPException(status_code=404, detail="Invalid Entry")
        if rows["role"] != "admin":
            raise HTTPException(status_code=403, detail="Access Forbidden")
        # for the dynamic UPDATE the in the admin fields
        pieces = []
        values = []
        if entry.clock_in is not None:
            pieces.append("clock_in=%s") # holds string
            values.append(entry.clock_in) # holds data
        if entry.clock_out is not None:
            pieces.append("clock_out=%s")
            values.append(entry.clock_out)
        if not pieces:
            raise HTTPException(status_code=400, detail="Invalid Entry")
        # putting the pieces together with join
        # clock_in , clock_out as strings
        joined_pieces = (",").join(pieces)
        await cur.execute(f"UPDATE shifts SET {joined_pieces} WHERE shift_id=%s RETURNING *", values + [shift_id],)
        admin_rows = await cur.fetchone()
        return admin_rows 