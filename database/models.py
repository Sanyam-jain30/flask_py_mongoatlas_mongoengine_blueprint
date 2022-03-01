from .db import db

class Customer(db.Document):
    contactID = db.UUIDField(required=True,binary=False)
    name = db.StringField(required=True)
    product = db.StringField(required=True)