# all worker routes the get hours and breakdown
from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_conn, verify_tokens
from datetime import date

router = APIRouter()

# the aggregation route
# COALESCE is a SQL function that takes a list of values and returns the first one that isn't NULL
# WHAT extract epoch from does is that it extracts the number out of the interval and EPOCH from is what asking to give the
# total as seconds; /3600 is plain division 3600 is an hour so this converts seconds to hour
# add the 403 route for ownership check
@router.get("/workers/{worker_id}/hours")
# borrowing the connection
async def hours(worker_id: int, hours_conn=Depends(get_conn), worker_tokens=Depends(verify_tokens)):
    # ownership check for the route
    if worker_tokens != worker_id:
        raise HTTPException(status_code=403, detail="Access Forbidden")
    async with hours_conn.cursor() as cur: # .cursor() creates a cursor on the connection
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (worker_id,)) # check againts no matching worker_id
        hour_rows = await cur.fetchone()
        if hour_rows is None:
            raise HTTPException(status_code=404, detail="Invalid Entry")
        await cur.execute("""
        SELECT ROUND(EXTRACT(EPOCH FROM COALESCE(SUM(clock_out - clock_in), INTERVAL '0')) /3600, 2) AS total_hours
        FROM shifts 
        WHERE worker_id=%s AND clock_out IS NOT NULL
        """, (worker_id,))
        hours = await cur.fetchone()
        return hours 

# aggregation route to see hours weekly and monthly
# returning filtered date hours
# every non default signature goes first
@router.get("/workers/{worker_id}/breakdown")
async def breakdown(worker_id: int, start: date , end: date, period: str ="weekly", 
                          hours_conn=Depends(get_conn), worker_tokens=Depends(verify_tokens)):
    # ownership check to confirm
    if worker_tokens != worker_id:
        raise HTTPException(status_code=403, detail="Access Forbidden")
    async with hours_conn.cursor() as cur:
        await cur.execute("""
              SELECT worker_id 
              FROM workers 
              WHERE worker_id=%s                          
              """, (worker_id,))
        computed_row = await cur.fetchone()
        if computed_row is None:
            raise HTTPException(status_code=404, detail="Invalid Entry")
# deploying a hanrdcoded dict instead of passing period in the query itself instead storing in a variable
        periods = {"weekly": "week", "monthly": "month"}
        if period not in periods:
            raise HTTPException(status_code=400, detail="wrong input value")
        trunc = periods[period]
        if start >= end:
            raise HTTPException(status_code=400, detail="wrong input value")
        # f string to call the period as a keyword in SQL
        # wrapped the date_trunc in to_char to format the timestamp into a readable string
        await cur.execute(f"""
        SELECT to_char(date_trunc('{trunc}', clock_in), 'YYYY Mon DD') AS period_start,
            ROUND(EXTRACT (EPOCH FROM COALESCE(SUM(clock_out - clock_in), INTERVAL '0')) /3600, 2) AS total_hours
        FROM shifts
        WHERE worker_id=%s AND clock_out IS NOT NULL AND clock_in >= %s AND clock_in < %s
        GROUP BY date_trunc('{trunc}', clock_in)
        ORDER BY date_trunc('{trunc}', clock_in)
        """, (worker_id, start, end,))
        period_rows = await cur.fetchall()
        return period_rows