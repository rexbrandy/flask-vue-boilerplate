from flask import Flask
from flask_migrate import Migrate

from api.config import Config
from api.models import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)