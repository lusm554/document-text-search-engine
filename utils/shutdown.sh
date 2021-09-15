#!/bin/bash
docker-compose -p text_search_engine down
rm -rf pgdata
rm -rf esdata
docker volume prune --force
