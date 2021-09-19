import asyncio
from src.db import Postgres, Elastic

class DAO(object):
    def __init__(self, pgtable='documents'):
        self.pg = Postgres()
        self.es = Elastic()
        self.pgtable = pgtable

    async def __execute_pg_req__(self, query, args=()):
        try:
            conn = await self.pg.connect()
            rows = await conn.fetch(query, *args)
            return rows
        except Exception as pg_req_error:
            raise pg_req_error
        finally:
            await self.pg.close()

    async def __search_es__(self, body, index, size=20):
        try:
           es = self.es.connect() 
           docs = await es.search(index=index, body=body, size=size)
           return docs
        except Exception as es_req_error:
            raise es_req_error
        finally:
            await self.es.close()
