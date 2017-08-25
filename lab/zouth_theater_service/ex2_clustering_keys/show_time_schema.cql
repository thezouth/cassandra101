CREATE TABLE zouth_theater.showing_time(
    movie_id UUID,
    date DATE,
    start_time TIME,
    cinema TEXT,
    PRIMARY KEY ((movie_id, date), start_time, cinema)
) WITH CLUSTERING ORDER BY (start_time asc);