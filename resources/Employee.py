from flask import request
from flask_restful import Resource

from app import app
from external_services.dummy_client import DummyClient

dummy_client = DummyClient()


class Employee(Resource):
    def get(self):
        try:
            res = dummy_client.get_employees()
            employees = res.json()
            return {'success': True, 'data': employees}, 200
        except Exception as e:
            app.logger.exception('Get employee error in get employee route {}'.format(str(res)))
            return {'success': False, 'error': str(res)}, 400

    def post(self):
        try:
            post_data = request.get_json(force=True)
            res = dummy_client.create_employee(post_data)
            employee = res.json()
            return {'success': True, 'data': employee}, 201
        except Exception as e:
            app.logger.exception('Post employee error {}'.format(str(res)))
            return {'success': False, 'error': str(res)}, 400
