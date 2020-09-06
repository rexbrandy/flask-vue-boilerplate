from flask import Flask
from flask_migrate import Migrate

from api.models import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)