#!/bin/bash

docker run --rm -it -v SCRIPT_DIR:/workspace --network cass-cluster python-cassandra:latest bash

