"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"


class Cupcake(db.Model):
    """Cupcake model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    photo_url = db.Column(db.Text)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def serialize(self):
        """Returns a dict representation of cupcake which we can turn into JSON"""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image
        }
