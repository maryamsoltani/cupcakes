"""Models for Cupcake app."""
import dbm
from email.policy import default
from unittest.mock import DEFAULT
from flask import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake "

class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = "cupcake"

    id = db.Column(db.Integer, Primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default=DEFAULT_IMAGE)

    def to_dict(self):

        return {
            "id":self.id,
            "flavor" : self.flavor,
            "rating": self.rating,
            "size":self.size,
            "image": self.image,
        }

        def connect_db(app):
            db.app = appdb.init_app(app)
            