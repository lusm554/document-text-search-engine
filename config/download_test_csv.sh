#!/bin/bash

CONFIGPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

curl -L "$CSV_FILE_URL" -o $CONFIGPATH/posts.csv

