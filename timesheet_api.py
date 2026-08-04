# THE DESIGN -
# 2 resources - workers and shifts
# workers model holds - name and workers_id -> assigned by the server and workers_id is also the primary key in workers
# and shifts model primary key is shift_id
# shift model holds - shift_id, workers_id and a shift needs two — clock-in and clock-out, 
# with clock-out starting empty. None in python or NULL in postgres
# The gaurds - it is against the updation of the clock-out, in the PUT route
# PUT /shifts/{shift_id}/clock-out
# the four gaurds: 1. Shift doesn't exist → 404
# 2. Already clocked out → 409
# 3. Not your shift → 403
# 4. Valid → 200, completed shift returned
# and now the whole clock out design -> clock out returns the hours for that shift and 
# a separte aggreagtion route that handles totals across shifts