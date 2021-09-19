from flask import Flask, Blueprint
from .routes import text_router

app = Flask(__name__)
app.url_map.strict_slashes = False

# prefix for api routes
api_bp = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api_bp.register_blueprint(text_router)
app.register_blueprint(api_bp)

@app.route('/')
def get_main():
   return 'OK', 200

