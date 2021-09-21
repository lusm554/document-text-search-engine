import asyncio
from .dao import DAO


class DocsDAO(DAO):
    def __init__(self, index='docs'):
        super(DocsDAO, self).__init__()
        self.index = 'docs'

    async def get_all(self, ids):
        # Probably exist fastest method for fetching rows like this
        query = 'select * from text where id = any($1::int[]) order by created_date'
        return await self.__execute_pg_req__(query, [ids])

    async def search(self, text):
        body = {
            'query': {
                'match': {
                    'text': text
                }
            },
            '_source': ['id']
        }
        return (await self.__search_es__(body, index=self.index))['hits']['hits']

    async def delete(self, id):
        query = 'delete from text where id = $1'
        body = {
            'index': self.index,
            'id': id
        }
        return await self.__delete_transaction__(body, query, id)

