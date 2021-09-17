#!/bin/bash
docker-compose -p text-search-engine down
docker image rm text-search-engine_web
rm -rf pgdata
rm -rf esdata
docker volume prune --force
docker network prune --force
