import requests

BASE_DUMMY_URL = "http://dummy.restapiexample.com/"


class DummyClient:

    def get_employees(self):
        return requests.get("{base_url}/api/v1/employees".format(base_url=BASE_DUMMY_URL))

    def create_employee(self, data):
        res = requests.post("{base_url}/api/v1/create".format(base_url=BASE_DUMMY_URL), json=data)
        return res
