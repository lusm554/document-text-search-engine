#!/bin/bash

# set .env vars
export $(echo $(cat ./config/.env | sed 's/#.*//g'| xargs) | envsubst)

sh config/download_test_csv.sh

