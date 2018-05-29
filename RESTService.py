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

    class InputValidator(object):
        @staticmethod
        def not_empty_str(s):
            if s == '':
                raise reqparse.exceptions.BadRequest("Param can not be empty")
            return s

        @staticmethod
        def positive_int(i):
            i = int(i)
            if i < 1:
                raise reqparse.exceptions.BadRequest("Param can not be empty")
            return i

    @staticmethod
    def reply(result):
        return {"result": result}
