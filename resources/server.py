from flask import Response, request
from database.models import Customer
from flask_restful import Resource
import uuid

class CustomersApi(Resource):
    def get(self):
        cus = Customer.objects().to_json()
        return Response(cus, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        cus = Customer()
        cus.name = body['name']
        cus.product = body['product']
        cus.contactID = uuid.uuid4()
        cus.save()
        return {'id': str(cus.contactID)}, 200

class CustomerApi(Resource):
    def put(self, id):
        body = request.get_json()
        Customer.objects().get(id=id).update(product=body['product'])
        return '', 200

    def delete(self, id):
        cus = Customer.objects().get(id=id).delete()
        return '', 200
