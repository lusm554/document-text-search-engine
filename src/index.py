from flask import Flask, Blueprint, Response
from .routes import text_router

app = Flask(__name__)
app.url_map.strict_slashes = False

# prefix for api routes
api_bp = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api_bp.register_blueprint(text_router)
app.register_blueprint(api_bp)

@app.route('/')
def get_main():
   return Response(response='OK', status=200)

@app.errorhandler(404)
def not_found(e):
    return Response(response='<h1>404</h1>', status=404)

