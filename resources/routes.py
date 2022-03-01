from .server import CustomersApi, CustomerApi

def initialize_routes(api):
    api.add_resource(CustomersApi, '/api/cus')
    api.add_resource(CustomerApi, '/api/cus/<id>')