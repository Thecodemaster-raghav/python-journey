# Timesheet API
Shift tracking for a small construction crew. Workers clock in and out; 
hours are computed from the timestamps.

## Resources
2 resources consisting workers and shifts, with workers schema having workers-id, role — string, defaults to "worker". The only other value is "admin". Server-assigned; clients cannot set it. workers also consist of a names field.

Shifts table consist of shift_id as primary key, having 2 clock-in clock-out timestmaps for workers
and foreign key in the shifts table worker_id is a foreign key referencing workers.worker_id

Connecting with postgres to eliminate the race condition which means having a gap within requests. Postgres introduces
atomic sequences which means no breaks in between operations. In python we used to read and then increment the data
which left a gap and that gap is what breaks atomic sequences.

### Each route
We have 4 different routes; 
1. POST /shifts -> this is where the data gets created a worker posts a
clock-in entry and that entry is created with a assigned id to the worker using the workers_id which is server assigned
and stays permanent for the worker. 
has different situations againsts it:
404 worker doesn't exist · 409 already has an open shift · 201 created data

2. PUT /shifts/{shift_id}/clock-out -> where the clock-out timing is updated and not created as it starts null and 
than gets updated.
404 shift doesn't exist · 409 already clocked out · 403 not your shift · 200 updated

3. PUT /shifts/{shift_id}/update-entry — admin correction; if recorded a missed punch. 
403 if role isn't admin

4. GET aggregation route — hours across shifts, computed on demand; where workers can access their data about
how many hours they have worked

#### Design decisions
1. Timestamps are server authoratative; if workers are able to edit or update changes than they could mis-report their hours.
2. Clock-out is a PUT not POST as we just want updating in the shift created; That is the reason it starts null and gets updated 
we do not want to create a separate POST for clock-out.
3. Admin correction is same reason as the timestamps we do not want to give access to workers to change their data or edit any changes so if any workers misses any shift they can just ask the admin to update their timestamp 
4. why role is server-assigned. If a client could set it, anyone registering could make themselves admin — privilege escalation