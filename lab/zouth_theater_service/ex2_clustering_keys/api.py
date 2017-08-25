'''
Objective: Learn how we query data on where with partition key.
'''
import uuid
import datetime as dt

from flask import jsonify, abort

from .. import app, cass_session


@app.route('/showing-movies/<movie_id>/show-times/<date_param>', methods=['GET'])
def get_showing_time(movie_id, date_param):
    '''
    Ex.2 Query showing time of movie by date
    Objective: Query with composite primary keys and clustering key
    '''
    date = dt.datetime.strptime(date_param, '%Y-%m-%d').date()

    if date == date.today():
        showing_times = cass_session.execute(
            '''
            [Fill your answer here!]
            ''',
            (uuid.UUID(movie_id), date, dt.datetime.now().time())
        )
    else:
        showing_times = cass_session.execute(
            '''
            [Fill your answer here!]
            ''',
            (uuid.UUID(movie_id), date)
        )

    return jsonify([
        {
            'startTime': show_time.start_time.time().strftime('%H:%M'),
            'cinema': show_time.cinema
        }
        for show_time in showing_times
    ])


@app.route('/showing-movies/<movie_id>/seats/<datetime>/<cinema>', methods=['GET'])
def get_seats(movie_id, datetime, cinema):
    date_object = dt.datetime.strptime(datetime, '%Y-%m-%dT%H:%M')
    query_param = (uuid.UUID(movie_id), date_object.date(), date_object.time(), cinema)

    seats = cass_session.execute(
        '''
        [Fill your answer here!]
        ''',
        query_param
    )

    # booked_seates_result = cass_session.execute(
    #     '[Fill your answer here!]',
    #     query_param
    # )

    # booked_seates_set = set(map(lambda seat: (seat.row, seat.col), booked_seates_result))
    
    booked_seates_set = set()

    return jsonify([
        {
            'row': seat.row,
            'col': seat.col,
            'seatType': seat.seat_type,
            'price': seat.price,
            'availability': not (seat.row, seat.col) in booked_seates_set
        }
        for seat in seats
    ])
