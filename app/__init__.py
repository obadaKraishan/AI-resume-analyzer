from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

def create_app():
    app = Flask(__name__, static_folder='main/static', template_folder='main/templates')
    app.config.from_object(Config)

    Bootstrap(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
