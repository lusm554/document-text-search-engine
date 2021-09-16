#!/bin/bash
docker-compose -p text_search_engine down
docker image rm text_search_engine_web
rm -rf pgdata
rm -rf esdata
docker volume prune --force
docker network prune --force
