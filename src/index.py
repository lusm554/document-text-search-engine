import asyncio
from flask import Flask, Blueprint
from src.routes import router

app = Flask(__name__)
app.url_map.strict_slashes = False

# How log smth in flask?
# Just use app.logger.info(data)

# prefix '/api/v1' for api routes
api_bp = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api_bp.register_blueprint(router)
app.register_blueprint(api_bp)

@app.route('/')
async def get_main():
    return 'OK', 200


