from flask import Flask
from flask_cors import CORS, cross_origin
from cassandra.cluster import Cluster

cass_cluster = Cluster(['localhost'])
cass_session = cass_cluster.connect('zouth_theater')

app = Flask(__name__)
CORS(app)

from .ex1_showing_movie import api as ex1_api
from .ex2_clustering_keys import api as ex2_api
from .ex3_lightweight_transaction import api as ex3_api
from .ex4_meterialize_view import api as ex4_api