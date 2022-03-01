from flask_mongoengine import MongoEngine
# from .api_constants import password

db = MongoEngine()

def initialize_db(app):
    db_name = # database name
    db_URI = # Mongo atlas connection link
    db.connect(host=db_URI)