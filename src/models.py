import asyncio
from src.db import create_postgres, Elastic

async def create_dao(table):
    dao = DAO(table)
    await dao._init()
    return dao

class DAO:
    def __init__(self, table):
        self.table = table

    async def _init(self):
        self.p = await create_postgres()

    async def __perform_db_req__(self, query):
        try:
            conn = await self.p.connect()
            row = await conn.fetchrow(query)
            return row
        except Exception as request_error:
            raise request_error
