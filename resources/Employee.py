from flask import jsonify, request
from flask_restful import Resource

from external_services.dummy_client import DummyClient

dummy_client = DummyClient()


class Employee(Resource):
    def get(self):
        employees = dummy_client.get_employees()
        return {
            'success': True,
            'data': employees
        }, 200


    def post(self):
        post_data = request.get_json(force=True)
        response = dummy_client.create_employee(post_data)
        return {
            'success': True,
            'data': response
        }, 201
