import uuid
import datetime as dt

from flask import jsonify, abort

from .. import app, cass_session


def get_movie_titles(movie_ids):
    def query():
        return [
            cass_session.execute_async(
                'SELECT id, title FROM showing_movie WHERE id = %s', 
                (movie_id,))
            for movie_id in movie_ids
        ]

    def parse_result(future_result_set):
        result = future_result_set.result()[0]
        return result.id, result.title

    return dict([
        parse_result(future_result_set)
        for future_result_set in query()
    ])


@app.route('/members/<member_id>/tickets')
def get_member_tickets(member_id):
    available_tickets = cass_session.execute(
        '''
        SELECT show_date, show_time, movie_id, cinema, row, col
        FROM ticket_by_member
        WHERE member_id = %s AND show_date >= %s
        ''',
        (member_id, dt.date.today())
    )

    if available_tickets:
        available_tickets_list = list(available_tickets)
        movie_titles = get_movie_titles(set(map(lambda t: t.movie_id, available_tickets_list)))

        return jsonify([
            { 
                'showDate': ticket.show_date.date().strftime('%Y-%m-%d'),
                'showTime': ticket.show_time.time().strftime('%H:%M'),
                'cinema': ticket.cinema,
                'movieId': ticket.movie_id,
                'movieTitle': movie_titles[ticket.movie_id],
                'row': ticket.row,
                'col': ticket.col   
            }
            for ticket in available_tickets_list
        ])
    else:
        return jsonify([])
