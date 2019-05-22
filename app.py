from flask import Flask, Blueprint
from flask_restful import Api

from resources.Employee import Employee

app = Flask(__name__)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Employee, '/employees')
