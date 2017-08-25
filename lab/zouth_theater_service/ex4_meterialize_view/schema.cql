CREATE MATERIALIZED VIEW ticket_by_member 
AS SELECT movie_id, show_date, show_time, cinema, row, col, member_id, price
FROM ticket_by_seat
WHERE movie_id IS NOT NULL AND show_date IS NOT NULL AND show_time IS NOT NULL AND cinema IS NOT NULL AND member_id IS NOT NULL AND row IS NOT NULL AND col IS NOT NULL
PRIMARY KEY ((member_id), show_date, show_time, movie_id, cinema, row, col);
