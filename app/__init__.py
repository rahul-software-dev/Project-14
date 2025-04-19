from flask import Flask
from config import Config
from app.db.session import init_db
from app.tasks.scheduler import init_celery
from app.api import api as api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    init_db(app)
    init_celery(app)

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app