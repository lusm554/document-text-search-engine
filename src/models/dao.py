import asyncio
from src.db import Postgres, Elastic
from elasticsearch import NotFoundError

class DAO(object):
    def __init__(self):
        self.pg = Postgres()
        self.es = Elastic()

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


    async def __delete_transaction__(self, body, query, id):
        try:
            # init transaction
            pg_conn = await self.pg.connect()
            es = self.es.connect()
            tr = pg_conn.transaction()
            await tr.start()
            
            # delete from postgres
            await pg_conn.execute(query, id)
            
            # delete from elastic
            try:
                res = await es.delete(**body)
            except NotFoundError:
                res = None
        except Exception as del_transaction_error:
            await tr.rollback()
            raise del_transaction_error
        else:
            await tr.commit()
        finally:
            await self.es.close()
            await self.pg.close()

