from datetime import datetime
from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    title = db.Column(db.String(70))
    add_time = db.Column(db.DateTime, default=datetime.now())
    new_data = db.Column(db.String(70))


