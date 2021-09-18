import asyncio
import json
from flask import Blueprint, Response, current_app as app
from src.models import create_dao

router = Blueprint('text', __name__, url_prefix='/text')
TextDAO = None

@router.before_request
async def defineTextDAO():
    global TextDAO
    if TextDAO == None:
        app.logger.info(1)
        TextDAO = await create_dao('text')

@router.route('/')
async def search():
    try:
        # return 'text', 200
        data = await TextDAO.__perform_db_req__('select * from text where id = 1')
        return data['text'], 200
    except Exception as e:
        app.logger.info(e)
        return Response(status=500)

@router.route('/', methods=['DELETE'])
async def delete():
    try:
        return 'plug\n', 200
    except:
        return Response(status=500)

