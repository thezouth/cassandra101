import pandas as pd
import uuid 

from cassandra.cluster import Cluster

cass_cluster = Cluster(['localhost'])
cass_session = cass_cluster.connect('zouth_theater')

source_data = pd.read_csv('movie-original.csv')

for idx, row in source_data.iterrows():
    movie_id = uuid.uuid1()
    title = row.movie_title
    genre = row.genre_list[1:-1].split(',')
    length = int(row.duration)

    cass_session.execute('''
        INSERT INTO showing_movie (id, title, genre, length)
        VALUES (%s, %s, %s, %s)
    ''', (movie_id, title, genre, length))

cass_session.shutdown()
cass_cluster.shutdown()
