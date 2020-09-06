from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.String(128))