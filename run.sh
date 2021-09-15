#!/bin/bash

# set .env vars
export $(echo $(cat ./config/.env | sed 's/#.*//g'| xargs) | envsubst)

sh config/download_test_csv.sh

docker-compose -f docker-compose.yml -p text_search_engine up -d 

