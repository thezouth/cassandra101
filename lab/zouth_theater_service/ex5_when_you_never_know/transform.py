import pandas as pd
import datetime as dt

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra.policies import RetryPolicy

cass_cluster = Cluster(['localhost'])
cass_session = cass_cluster.connect('zouth_theater')

query_statement = SimpleStatement(
    'SELECT movie_id, show_date, show_time, cinema, row, col, member_id, price FROM ticket_by_seat',
    consistency_level=ConsistencyLevel.ONE
)

result_set = cass_session.execute(query_statement)

def parse_record(record):
    return {
        'movie_id': record.movie_id,
        'show_date': record.show_date.date(),
        'show_time': record.show_time.time(),
        'cinema': record.cinema,
        'member_id': record.member_id,
        'price': record.price
    }

result_df = pd.DataFrame(list(map(parse_record, result_set)))

tickets_in_range = result_df[
    (result_df['show_date'] < dt.datetime.strptime('2017-09-15', '%Y-%m-%d').date())
    & (result_df['show_date'] >= dt.datetime.strptime('2017-08-15', '%Y-%m-%d').date())
]

ticket_count_by_member = tickets_in_range.groupby('member_id')['show_date'].count()
top_ticket_seat_member = ticket_count_by_member.sort_values(ascending=False).iloc[:3]

print('Top member buy most seats in this month')
print(top_ticket_seat_member)
print('\n')


money_paid_by_member = tickets_in_range.groupby('member_id')['price'].sum()
top_money_paid_member = money_paid_by_member.sort_values(ascending=False).iloc[:3]

print('Top member buy most values in thie month')
print(top_money_paid_member)
print('\n')
