'''
Objective: Learn how data distributed across several nodes with parition keys.
'''
import uuid

from flask import jsonify, abort

from .. import app, cass_session


@app.route('/showing-movies', methods=['GET'])
def list_showing_movies():
    '''Ex.1.1 Getting all movies from Cassandra'''
    all_movies = cass_session.execute('SELECT id, title FROM showing_movie')
    return jsonify([
        {'id': movie.id, 'title': movie.title}
        for movie in all_movies
    ])


@app.route('/showing-movies/<movie_id>', methods=['GET'])
def get_showing_movie(movie_id):
    '''
    Ex.1.2 Getting individual data from a specific movie.
    '''
    movies = cass_session.execute(
        'SELECT id, title, genre, length from showing_movie WHERE id = %s',
        (uuid.UUID(movie_id),)
    )

    if movies:
        movie = movies[0]
        return jsonify({
            'id': movie.id,
            'title': movie.title,
            'genre': movie.genre,
            'length': movie.length
        })
    else:
        return abort(404)
