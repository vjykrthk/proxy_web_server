import requests

from app import app

BASE_DUMMY_URL = "http://dummy.restapiexample.com/"


class DummyClient:

    def get_employees(self):
        res = requests.get("{base_url}/api/v1/employees".format(base_url=BASE_DUMMY_URL))
        app.logger.info('Get employees client request status - {} response - {}'.format(
            res.status_code,
            str(res)
        ))
        return res

    def create_employee(self, data):
        res = requests.post("{base_url}/api/v1/create".format(base_url=BASE_DUMMY_URL), json=data)
        app.logger.info('Create employee client request status - {} response - {}'.format(
            res.status_code,
            str(res)
        ))
        return res
