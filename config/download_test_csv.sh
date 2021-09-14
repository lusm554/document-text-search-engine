#!/bin/bash

CSV_FILE="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"/posts.csv

if ! [ -f "$CSV_FILE" ]; then
  curl -L "$CSV_FILE_URL" -o $CSV_FILE 
fi

