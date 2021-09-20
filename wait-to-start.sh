#!/bin/bash

echo $WAIT_COMMAND
echo $WAIT_START_CMD

TRIES_COUNT=200

is_index_ready() {
  #eval "[ $(curl -s -o /dev/null -w "%{http_code}" localhost:9200/docs) = 200 ]"
  eval "$WAIT_COMMAND"
}

i=0
while ! is_index_ready; do
  if [ $i -ge $TRIES_COUNT ]; then
    echo "$(date) - elastic still not ready, giving up."
    exit 1
  fi
  echo "$(date) - waiting for elastic to be ready $((i*2)) seoncds. Yeah, logstash slowly load data from postgres to elasticsearch."
  i=`expr $i + 1`
  sleep 2
done

exec $WAIT_START_CMD

