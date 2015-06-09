from datetime import datetime
from .. import db

class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(255), unique=True)
    body = db.Column(db.Text())

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow,
                                          onupdate=datetime.utcnow)

    def __init__(self, headline="", body=""):
        self.headline = headline
        self.body = body

    def __repr__(self):
        return '<Banner - {}>'.format(self.headline)
