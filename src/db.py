import asyncio
import asyncpg
from elasticsearch import AsyncElasticsearch
from src.config import PG_USER, PG_PWD, PG_HOSTNAME, PG_PORT, PG_DB
from flask import current_app as app

async def create_postgres():
    postgres = Postgres()
    await postgres._init()
    return postgres

class Postgres:
    def __init__(self):
        self.url = f'postgresql://{PG_USER}:{PG_PWD}@{PG_HOSTNAME}:{PG_PORT}/{PG_DB}'

    async def _init(self):
        # add postgres pool to global app object
        app.config['pool'] = await asyncpg.create_pool(self.url)

    async def connect(self):
        pool = app.config.get('pool')
        conn = await pool.acquire()
        return conn

class Elastic:
    pass

