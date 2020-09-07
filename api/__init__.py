from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from api.config import Config
from api.example import example_bp
from api.models import db

migrate = Migrate()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    cors.init_app(app, resources={r'/*': {'origins': '*'}})

    app.register_blueprint(example_bp)

    return app