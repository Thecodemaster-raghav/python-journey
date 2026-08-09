-- schema for workers table
CREATE TABLE workers(
    name text NOT NULL, --name can not be null
    worker_id integer NOT NULL PRIMARY KEY,
    role text NOT NULL DEFAULT 'worker',
    CHECK (role ())
);

--schema for shifts table 
CREATE TABLE shifts(
    shift_id integer PRIMARY KEY, -- the unique and not null column in the shifts table
    worker_id integer NOT NULL REFERENCES workers, -- foreign key referenceing workerr_id in workers table
    clock_in timestamp with time zone NOT NULL, -- DESIGN RULE OF NOT KEEPING CLOCK_IN NULL
    clock_out timestamp with time zone NULL, -- clock_out gets updated usin PUT route so keeping it null
    CHECK (clock_out > clock_in) -- clock_in time can never be greater than clocl_out as it would affect the aggregate hours
); -- and it is a table constraint as it has 2 columns involved 
