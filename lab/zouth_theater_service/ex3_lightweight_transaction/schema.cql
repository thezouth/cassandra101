CREATE TABLE ticket_by_seat(
    movie_id UUID,
    show_date DATE,
    show_time TIME,
    cinema TEXT,
    row ASCII,
    col SMALLINT,
    member_id TEXT,
    price INT,
    PRIMARY KEY ((movie_id, show_date, show_time, cinema), row, col)
) WITH CLUSTERING ORDER BY (row ASC, col ASC);