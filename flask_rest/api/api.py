#!/usr/bin/env python3
from flask import Flask, request, g
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return 'works'

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)