from Registry import *
from flask import Flask
from flask_restful import Resource, Api, reqparse


class RESTService(Resource):
    def __init__(self):
        self.registry = Registry()
        self.parser = reqparse.RequestParser()

    @staticmethod
    def start():
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(RESTService, '/api/services')
        app.run(port='5002')
