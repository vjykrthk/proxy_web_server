from flask import request
from flask_restful import Resource

from external_services.dummy_client import DummyClient

dummy_client = DummyClient()


class Employee(Resource):
    def get(self):
        res = dummy_client.get_employees()
        employees = res.json()
        try:
            return {
                       'success': True,
                       'data': employees
                   }, 200
        except Exception as e:
            return {
                       'success': False,
                       'error': str(res.content)
                   }, 400

    def post(self):
        try:
            post_data = request.get_json(force=True)
            response = dummy_client.create_employee(post_data)
            employee = response.json()
            return {'success': True, 'data': employee}, 201
        except Exception as e:
            return {'success': False, 'error': str(response.content)}, 400
