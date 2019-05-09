#!/bin/bash
docker network create cass-cluster
docker run --name cassandra --network cass-cluster -d cassandra:3.11.4

