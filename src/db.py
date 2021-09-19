import asyncio
import asyncpg
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
        self.a = ES_INDEX
        self.conn_settings = [
            {'host': ES_HOSTNAME, 'port': ES_PORT}
        ]
        self.es = None

    def connect(self):
        self.es = AsyncElasticsearch(self.conn_settings)
        return self.es

    async def close(self):
        await self.es.close()

