import datetime as dt
import uuid 
import random

from cassandra.cluster import Cluster


one_day = dt.timedelta(days=1)
show_time_set = [
    {dt.time(10, 30), dt.time(15,  0), dt.time(18, 20)},
    {dt.time(11, 00), dt.time(14, 10), dt.time(18, 25), dt.time(20, 20)},
    {dt.time(10, 15), dt.time(12,  0), dt.time(14, 25), dt.time(17, 20), dt.time(21, 10)}
]
cinema_list = ['cinema1', 'cinema2', 'cinema3', 'cinema4']


def random_showing_times(movie_count):
    for cinema in cinema_list:
        for show_times in show_time_set:
            movie_idx = random.randint(0, movie_count - 1)
            
            for show_time in show_times:
                yield (movie_idx, show_time, cinema)


def generate_showing_times(movies, date_count=30):
    movie_count = len(movies)
    date = dt.date.today()

    for date_shift in range(date_count):
        result = list(
            map(lambda row: (movies[row[0]], date, row[1], row[2]), 
            random_showing_times(movie_count))
        )
        yield from result
        date = date + one_day


cass_cluster = Cluster(['localhost'])
cass_session = cass_cluster.connect('zouth_theater')

all_movies = list(map(
    lambda i: i.id,
    list(cass_session.execute('SELECT id FROM showing_movie'))
))

showing_times = generate_showing_times(all_movies, 30)

## most direct way to go.
# for time in showing_times:
#     cass_session.execute('''
#         INSERT INTO showing_time(movie_id, date, start_time, cinema)
#         VALUES (%s, %s, %s, %s)
#     ''', time)

## alternative on performance, and reuse statemtent on different of time.
# prepared_stmt = cass_session.prepare('''
#         INSERT INTO showing_time(movie_id, date, start_time, cinema)
#         VALUES (?, ?, ?, ?)
# ''')
# for time in showing_times:
#     cass_session.execute(prepared_stmt, time)

# very high performance, execute them asyc.
prepared_stmt = cass_session.prepare('''
        INSERT INTO showing_time(movie_id, date, start_time, cinema)
        VALUES (?, ?, ?, ?)
''')

result_sets = []

for time in showing_times:
    result_sets.append(cass_session.execute_async(prepared_stmt, time))

for result_set in result_sets:
    result_set.result()


cass_session.shutdown()
cass_cluster.shutdown()
