#!/bin/bash
docker run --rm -it --network cass-cluster cassandra:3.11.4 cqlsh cassandra

