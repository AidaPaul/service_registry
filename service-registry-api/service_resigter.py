#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import array
app = Flask(__name__)


	  
services = [
    {
        'id': 1,
		'uniqueID' : u'0.0.1.1.epochtime',
        'service': u'test',
        'version': u'0.0.1', 
        'change': u'created'
    },
    {
        'id': 2,
		'uniqueID' : u'0.0.1.2.epochtime',
        'service': u'test',
	    'version': u'0.0.1', 
        'change': u'created'
    },
	{
        'id': 3,
		'uniqueID' : u'0.0.2.1.epochtime',
        'service': u'test',
        'version': u'0.0.2', 
        'change': u'created'
    },
    {
        'id': 4,
		'uniqueID' : u'0.0.2.2.epochtime',
        'service': u'test',
	    'version': u'0.0.2', 
        'change': u'created'
    },
    {
        'id': 5,
		'uniqueID' : u'0.0.2.1.epochtime',
        'service': u'test2',
	    'version': u'0.0.2', 
        'change': u'created'
    },
	    {
        'id': 6,
		'uniqueID' : u'0.0.2.2.epochtime',
        'service': u'test2',
	    'version': u'0.0.2', 
        'change': u'created'
    }
]


@app.route('/service_registry/api/v1.0/findServices', methods=['GET'])
def get_services():
    return jsonify({'services': services})
@app.route('/service_registry/api/v1.0/findServices/<int:service_id>', methods=['GET'])
def get_service_id(service_id):
    service = [service for service in services if service['id'] == service_id]
    if len(service) == 0:
        abort(404)
    return jsonify({'service': service[0]})
	
@app.route('/service_registry/api/v1.0/findServices/<service_name_all>/getAll', methods=['GET'])
def get_service_all(service_name_all):
    service = [service for service in services if service['service'] == service_name_all]
    if len(service) == 0:
        abort(404)
    return jsonify({'service': service})
	
@app.route('/service_registry/api/v1.0/findServices/<service_name>', methods=['GET'])
def get_service(service_name):
    service = [service for service in services if service['service'] == service_name]
    if len(service) == 0:
            return jsonify({'service': service_name,'count': 0 })
    count=len(service)	
    return jsonify({'service': service_name,'count': count })
@app.route('/service_registry/api/v1.0/findServices/<service_name>/<service_version>', methods=['GET'])
def get_service_count(service_name,service_version):
    service = [service for service in services if service['service'] == service_name and service['version'] == service_version]
    if len(service) == 0:
            return jsonify({'service': service_name, 'version' : 'service_version', 'count': 0 })
    count=len(service)	
    #return jsonify({'service': service})	
    return jsonify({'service': service_name, 'version' : 'service_version', 'count': count })
	


	
if __name__ == '__main__':
    app.run(debug=True)
