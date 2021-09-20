from src.models.docs import DocsDAO
import asyncio
import json
from flask import (
    Blueprint, 
    Response,
    request as req, 
    current_app as app # remove
)

router = Blueprint('text', __name__, url_prefix='/')
Docs = DocsDAO()

@router.before_request
async def validation():
    search_endpoint = 'api-v1.text.search'
    if req.endpoint == search_endpoint:
        if not req.args.get('text'):
            return Response(status=400)
        if len(req.args.get('text')) > 100:
            return Response(status=414)


@router.route('/search')
async def search():
    try:
        text = req.args.get('text')
        docs = await Docs.search(text)
        ids = [int(doc['_source']['id']) for doc in docs]
        rows = await Docs.get_all(ids)
        rows = [dict(row.items()) for row in rows]
        return json.dumps(rows, ensure_ascii=False, default=str)
    except Exception as e:
        # raw method of handle elastic connection timeout
        if str(e) == 'ConnectionTimeout caused by - TimeoutError()':
            msg = 'Most likely the server did not manage to exit the idle state, please try again.'
            return Response(response=msg, status=408)
        return Response(status=500)


@router.route('/<id>', methods=['DELETE'])
async def delete(id):
    try:
        app.logger.info(f'delete id = {id}')
        await Docs.delete(int(id))
        return Response(status=204) # in any case: if item already deleted or deleted not 
    except Exception as e:
        app.logger.info(e)
        return Response(status=500)

