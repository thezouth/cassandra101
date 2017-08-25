CREATE TABLE seat (
    movie_id UUID,
    date DATE,
    start_time TIME,
    cinema TEXT,
    row ASCII,
    col SMALLINT,
    seat_type TEXT,
    price INT,
    PRIMARY KEY ((movie_id, date, start_time, cinema), row, col)
) WITH CLUSTERING ORDER BY (row ASC, col ASC);
