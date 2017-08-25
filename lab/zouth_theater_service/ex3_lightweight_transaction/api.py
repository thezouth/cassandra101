import uuid
import datetime as dt

from flask import jsonify, abort, request

from .. import app, cass_session

@app.route('/showing-movies/<movie_id>/seats/<datetime>/<cinema>/book/<row>/<int:col>', methods=['POST'])
def book_seat(movie_id, datetime, cinema, row, col):
    request_param = request.json
    member_id = request_param['memberId']
    price = request_param['price']

    date_object = dt.datetime.strptime(datetime, '%Y-%m-%dT%H:%M')

    result_set = cass_session.execute(
        '''
        [Fill your answer here!]
        ''',
        (uuid.UUID(movie_id), date_object.date(), date_object.time(), cinema, row, col, member_id, price)
    )

    executed = (not result_set) or result_set.was_applied
    if executed:
        return 'done', 200
    else:
        return abort(409)