import asyncio
import asyncpg
import requests
from elasticsearch import AsyncElasticsearch
from src.config import (
    PG_USER, 
    PG_PWD, 
    PG_HOSTNAME, 
    PG_PORT, 
    PG_DB,
    ES_HOSTNAME,
    ES_PORT,
    ES_INDEX
)

class Postgres:
    def __init__(self):
        self.url = f'postgresql://{PG_USER}:{PG_PWD}@{PG_HOSTNAME}:{PG_PORT}/{PG_DB}'
        self.conn = None

    async def connect(self):
        self.conn = await asyncpg.connect(self.url)
        return self.conn
    
    async def close(self):
        await self.conn.close()

class Elastic:
    def __init__(self):
        self.conn_settings = [
            {'host': ES_HOSTNAME, 'port': ES_PORT}
        ]
        self.es = None
        self.__set_dynamic_index_settings__()

    def __set_dynamic_index_settings__(self):
        body = {
            'index': { 'search': { 'idle': { 'after': 3600 } } }
        }
        r = requests.get(
            f'http://{ES_HOSTNAME}:{ES_PORT}/{ES_INDEX}/_settings',
            json=body
        )
        assert r.status_code == 200

    def connect(self):
        self.es = AsyncElasticsearch(self.conn_settings)
        return self.es

    async def close(self):
        await self.es.close()

