from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {'about': 'Home Page'}

    def post(self):
        json = request.get_json()
        return {'You sent:': json}, 201


class Calculate(Resource):
    def get(self, num):
        return {'result:': num*10}


api.add_resource(Home, '/')
api.add_resource(Calculate, '/api/v1/calculate/<int:num>')
