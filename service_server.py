from functools import wraps

from flask import Flask, jsonify, make_response, redirect, request
from flask_restful import Api, reqparse, Resource
from pony import orm
from werkzeug.exceptions import BadRequest

# Configuration
PROVIDER = 'sqlite'
CREATE_DB = True
DATABASE = 'database.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)

# database and models
db = orm.Database()


class ServiceRegistry(db.Entity):
    _table_ = 'services'

    id = orm.PrimaryKey(int, auto=True)
    service = orm.Required(str)
    version = orm.Optional(str)
    change = orm.Required(str)


# helper methods
def sortkeypicker(keynames):
    # https://stackoverflow.com/a/1143719/311829
    negate = set()
    for i, k in enumerate(keynames):
        if k[:1] == '-':
            keynames[i] = k[1:]
            negate.add(k[1:])

    def getit(adict):
        composite = [adict[k] for k in keynames]
        for i, (k, v) in enumerate(zip(keynames, composite)):
            if k in negate:
                composite[i] = -v
        return composite
    return getit


def errors_handler(view):
    @wraps(view)
    def wrapped(self, *f_args, **f_kwargs):
        try:
            return view(self, *f_args, **f_kwargs)
        except orm.ObjectNotFound as e:
            return make_response(jsonify({
                'status': False,
                'message': 'Resource Not Found'
            }), 404)
        except Exception as e:
            return make_response(jsonify({
                'status': False,
                'message': 'Internal Server Error: ' + str(e)
            }), 505)
    return wrapped


# requires both service and version params
service_parser = reqparse.RequestParser(bundle_errors=True)
service_parser.add_argument(
    'service', type=str,
    help='Service name has to be provided',
    required=True
)
service_parser.add_argument(
    'version', type=str,
    help='Version value has to be provided',
    required=True
)


# rest resources
class ServiceResourceList(Resource):

    # @errors_handler
    @orm.db_session
    def get(self):
        data = request.values
        if len(list(data.keys())) == 0:
            # no params to query
            query = ServiceRegistry.select()
        elif ('service' in data and data['service']) and ('version' in data and data['version']):
            # filtering by service and version
            query = orm.select(
                c for c in ServiceRegistry
                if c.service == data['service'] and c.version == data['version'])
        elif ('service' in data and data['service']):
            # filtering by only service
            query = orm.select(
                c for c in ServiceRegistry
                if c.service == data['service'])
        return {
            'status': True,
            'items': sorted([
                item.to_dict()
                for item in query],
                key=sortkeypicker(('service', 'version', 'change'))
            )}

    @errors_handler
    @orm.db_session
    def put(self):
        try:
            values = service_parser.parse_args()
        except BadRequest as e:
            err_response = {'status': False}
            err_response.update(e.data)
            return make_response(jsonify(err_response), 400)

        service = ServiceRegistry(
            service=values['service'],
            version=values['version'],
            change='created'
        )
        db.commit()
        return redirect('/services/' + str(service.id))


class ServiceResource(Resource):
    @errors_handler
    @orm.db_session
    def get(self, service_id):
        service = ServiceRegistry[service_id]

        if service:
            return make_response(jsonify({
                'status': True,
                'message': 'Resource Found',
                'item': service.to_dict()
            }), 200)

    @errors_handler
    @orm.db_session
    def delete(self, service_id):
        service = ServiceRegistry[service_id]

        if service:
            service.change = 'removed'
            db.commit()
            return make_response(jsonify({
                'status': True,
                'message': 'Successfully deleted. ID [{}]'.format(service_id),
                'item': service.to_dict()
            }), 200)

    @errors_handler
    @orm.db_session
    def put(self, service_id):
        if not service_id:  # insert
            try:
                values = service_parser.parse_args()
            except BadRequest as e:
                err_response = {'status': False}
                err_response.update(e.data)
                return make_response(jsonify(err_response), 400)

            service = ServiceRegistry(
                service=values['service'],
                version=values['version'],
                change='created'
            )
            db.commit()
            return redirect('/services/' + str(service.id))
        else:  # update
            service = ServiceRegistry[service_id]

            if service:
                if request.form.get('service') is not None:
                    service.service = request.form['service']
                if request.form.get('version') is not None:
                    service.version = request.form['version']
                service.change = 'changed'
                db.commit()
                return make_response(jsonify({
                    'status': True,
                    'message': 'Resource updated',
                    'item': service.to_dict()
                }), 200)


api = Api(app)
api.add_resource(ServiceResourceList, '/services', strict_slashes=False)
api.add_resource(ServiceResource, '/services/<string:service_id>', strict_slashes=False)


def init_db(app):
    db.bind(
        provider=app.config['PROVIDER'],
        filename=app.config['DATABASE'],
        create_db=app.config['CREATE_DB']
    )
    db.generate_mapping(create_tables=True)
    return db


if __name__ == '__main__':
    db = init_db(app)
    app.run(debug=app.config['DEBUG'])
