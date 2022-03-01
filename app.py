from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from database.models import Customer
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

initialize_db(api)
initialize_routes(api)

app.run()