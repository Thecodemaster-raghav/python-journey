# all shift routes 
from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_conn, verify_tokens

router = APIRouter()

# POST /shifts route with 2 gaurds where Guard 1 fails when it finds nothing (worker missing). 
# Guard 2 fails when it finds something (open shift exists).
# we get worker_id from the tokens itself now so need for the model for shift with worker id so that
# no other worker can edit other workers shift timings
@router.post("/shifts")
async def WorkerShift(new_con= Depends(get_conn), current_worker=Depends(verify_tokens)):
    async with new_con.cursor() as cur:
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (current_worker,))
        fetch_worker_row = await cur.fetchone()
        if fetch_worker_row is None:
            raise HTTPException(status_code=404, detail="no matching workers found")
        await cur.execute("SELECT worker_id FROM shifts WHERE worker_id=%s AND clock_out IS NULL", (current_worker,))
        fetch_shift_row = await cur.fetchone()
        if fetch_shift_row is not None:
            raise HTTPException(status_code=409, detail="dual shift entry")
        await cur.execute("INSERT INTO shifts (worker_id, clock_in) VALUES (%s, now()) RETURNING *", (current_worker,))
        shift_data = await cur.fetchone()
        return shift_data

# PUT route for shift clock_out with gaurds 
# 404 shift doesn't exist · 409 already clocked out · 403 not your shift · 200 updated
# to merger both the gaurds i needed to select clock_out and filter on shift_id; clock_out starts as null
@router.put("/shifts/{shift_id}/clock_out")
async def clockOut(shift_id: int, conn_ClockOut=Depends(get_conn), worker_tokens=Depends(verify_tokens)):
    async with conn_ClockOut.cursor() as cur:
        await cur.execute("SELECT clock_out, worker_id FROM shifts WHERE shift_id=%s", (shift_id,))
        clockOut_rows = await cur.fetchone()
        if clockOut_rows is None:
            raise HTTPException(status_code=404, detail="no shift exist")
        # the ownership check
        if clockOut_rows["worker_id"] != worker_tokens:
            raise HTTPException(status_code=403, detail="Access Forbidden")
        if clockOut_rows["clock_out"] is not None: # as the clockOut_rows is a dict row
            raise HTTPException(status_code=409, detail="clocked out exist already")
        await cur.execute("UPDATE shifts SET clock_out = now() WHERE shift_id=%s RETURNING *", (shift_id,)) # no insert 
        # as we are updating the table not inserting values
        clockOut_update = await cur.fetchone()
        return clockOut_update