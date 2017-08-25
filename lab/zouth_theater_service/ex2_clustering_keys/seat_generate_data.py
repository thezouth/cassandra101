import datetime as dt
import uuid 
import random

from cassandra.cluster import Cluster

STANDARD_ROW = 4
DELUX_ROW = 1
START_ROW = ord('a')

COL = 10

NORMAL_STANDARD_PRICE = 180
NORMAL_DELUX_PRICE = 250

DISCOUNT_STANDARD_PRICE = 100
DISCOUNT_DELUX_PRICE = 170

WEDNESDAY = 2


def create_seats(discount=False):
    standard_price = NORMAL_STANDARD_PRICE if not discount else DISCOUNT_STANDARD_PRICE
    delux_price = NORMAL_DELUX_PRICE if not discount else DISCOUNT_DELUX_PRICE

    for row in range(STANDARD_ROW):
        for col in range(COL):
            yield chr(START_ROW + row), col + 1, 'standard', standard_price

    for row in range(DELUX_ROW):
        for col in range(COL):
            yield chr(START_ROW + STANDARD_ROW + row), col + 1, 'delux', delux_price


def generate_data(show_times):
    for show_time in show_times:
        date = show_time.date
        discount = date.date().weekday() == WEDNESDAY

        original_data = (show_time.movie_id, show_time.date, show_time.start_time, show_time.cinema,)

        yield from map(
            lambda result: original_data + result,
            create_seats(discount)
        )


cass_cluster = Cluster(['localhost'])
cass_session = cass_cluster.connect('zouth_theater')

all_show_times = cass_session.execute('SELECT * FROM showing_time')
all_seats = generate_data(all_show_times)

# very high performance, send with bulk statements.
prepared_stmt = cass_session.prepare('''
        INSERT INTO seat(movie_id, date, start_time, cinema, row, col, seat_type, price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''')

result_sets = []

for seat in all_seats:
    result_sets.append(cass_session.execute_async(prepared_stmt, seat))

for result_set in result_sets:
    result_set.result()


cass_session.shutdown()
cass_cluster.shutdown()
