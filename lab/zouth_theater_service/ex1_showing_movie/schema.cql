CREATE KEYSPACE zouth_theater WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};

CREATE TABLE zouth_theater.showing_movie (
    id UUID PRIMARY KEY,
    title TEXT,
    genre LIST<TEXT>,
    length INT
);