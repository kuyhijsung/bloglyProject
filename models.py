from flask_sqlalchemy import SQLAlchemy
"""Models for Blogly."""
db = SQLAlchemy()

class User(db.Model):
    """Users Data"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def connect_db(app):
    db.app = app
    db.init_app(app)
