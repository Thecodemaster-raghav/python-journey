--schema for shifts table 
CREATE TABLE shifts (
    shift_id serial PRIMARY KEY, --primary key requires values to be both not null and unique
    worker_id integer NOT NULL REFERENCES workers (worker_id), --in this case we are referencing to workers_id in workers table. 
    -- which is our foreign key
    clock_in timestamp with time zone NOT NULL,
    clock_out timestamp with time zone NULL,
    CHECK (clock_out > clock_in) --putting a table constraint so that the clock_out time can never be smaller than the clock_in
    -- time
);