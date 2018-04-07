#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import array
from flask import request
from flask import make_response
from flask import url_for


app = Flask(__name__)


#We use a temporary in memory json object to store the services
#This of course should be on a DB in the long term.	  
services = [
    {
        'id': 1,
#		'uniqueID' : u'0.0.1.1.epochtime',
        'change_version':1, 
        'service': u'test',
        'version': u'0.0.1', 
        'change': u'created'
    },
    {
        'id': 2,
#		'uniqueID' : u'0.0.1.2.epochtime',
        'change_version':1,
        'service': u'test',
	    'version': u'0.0.1', 
        'change': u'created'
    },
	{
        'id': 3,
#		'uniqueID' : u'0.0.2.1.epochtime',
        'change_version':1,
        'service': u'test',
        'version': u'0.0.2', 
        'change': u'created'
    },
    {
        'id': 4,
#		'uniqueID' : u'0.0.2.2.epochtime',
        'change_version':1,
        'service': u'test',
	    'version': u'0.0.2', 
        'change': u'created'
    },
    {
        'id': 5,
#		'uniqueID' : u'0.0.2.1.epochtime',
        'change_version':1,
        'service': u'test2',
	    'version': u'0.0.2', 
        'change': u'created'
    },
	    {
        'id': 6,
#		'uniqueID' : u'0.0.2.2.epochtime',
        'change_version':1,
        'service': u'test2',
	    'version': u'0.0.2', 
        'change': u'created'
    }
]

#This is our get function at the high level. This will return a json object including all registered services.
#We also return a URI refering to each service so that the users don't have to create that
@app.route('/service_registry/api/v1.0/services', methods=['GET'])
def get_services():
    return jsonify({'services': services})
#put the code below in once you get URIs working
#     return jsonify({'services': [make_public_service(service) for service in services]})

#This get function returns a service by service id
@app.route('/service_registry/api/v1.0/services/<int:service_id>', methods=['GET'])
def get_service_id(service_id):
    service = [service for service in services if service['id'] == service_id]
    if len(service) == 0:
        abort(404)
    return jsonify({'service': service[0]})
#This end point returns all instances and versions for a given service
@app.route('/service_registry/api/v1.0/services/<service_name_all>/getAll', methods=['GET'])
def get_service_all(service_name_all):
    service = [service for service in services if service['service'] == service_name_all]
    if len(service) == 0:
        abort(404)
    return jsonify({'service': service})
	



#This returns the count of a given service
@app.route('/service_registry/api/v1.0/services/<service_name>', methods=['GET'])
def get_service(service_name):
    service = [service for service in services if service['service'] == service_name]
    if len(service) == 0:
            return jsonify({'service': service_name,'count': 0 })
    count=len(service)	
    return jsonify({'service': service_name,'count': count })
#this returns the counts of a service and version
@app.route('/service_registry/api/v1.0/services/<service_name>/<service_version>', methods=['GET'])
def get_service_count(service_name,service_version):
    service = [service for service in services if service['service'] == service_name and service['version'] == service_version]
    if len(service) == 0:
            return jsonify({'service': service_name, 'version' : service_version ,'Not found':'True', 'count': 0 })
    count=len(service)	
    #return jsonify({'service': service})	
    return jsonify({'service': service_name, 'version' : service_version, 'count': count })
	

#return a nice message if not found
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

	#This is the post end point implementation
@app.route('/service_registry/api/v1.0/services', methods=['POST'])
def create_service():
    if not request.json or not 'service' in request.json or not 'version' in request.json:
        abort(400)
    service = {
        'id': services[-1]['id'] + 1,
        'change_version':1,
        'service': request.json['service'],
        'version': request.json.get('version', ""),
#        'uniqueID' : u'0.0.2.2.epochtime',
        'change': u'created'
    }
    services.append(service)
    return jsonify({'service': service}), 201

    

#This is the update service using the service id
#Other types of update needs to be implemented
@app.route('/service_registry/api/v1.0/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = [service for service in services if service['id'] == service_id]
    if len(service) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'service' in request.json and type(request.json['service']) != str:
        abort(400)
    if 'version' in request.json and type(request.json['version']) != str:
        abort(400)
    if 'change' in request.json and type(request.json['change']) != str:
        abort(400)
    service[0]['service'] = request.json.get('service', service[0]['service'])
    service[0]['version'] = request.json.get('version', service[0]['version'])
    service[0]['change'] = u'changed'
    service[0]['change_version']=service[0]['change_version']+1
    return jsonify({'service': service[0]})

#This is the put implementation for /services/service_name
@app.route('/service_registry/api/v1.0/services/<service_name>', methods=['PUT'])
def update_service_serviceName(service_name):
    service = [service for service in services if service['service'] == service_name]
    if len(service) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'service' in request.json and type(request.json['service']) != str:
        abort(400)
    if 'version' in request.json and type(request.json['version']) != str:
        abort(400)
    if 'change' in request.json and type(request.json['change']) != str:
        abort(400)

    for i in range(0,len(service)):
        service[i]['service'] = request.json.get('service', service[i]['service'])
        service[i]['version'] = request.json.get('version', service[i]['version'])
        service[i]['change'] = u'changed'
        service[i]['change_version']=service[i]['change_version']+1

    return jsonify({'service': service})

#This is the put implementation for /services/service_name/version_name
@app.route('/service_registry/api/v1.0/services/<service_name>/<service_version>', methods=['PUT'])
def update_service_serviceName_versionName(service_name,service_version):
    service = [service for service in services if service['service'] == service_name and service['version'] == service_version]
    if len(service) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'service' in request.json and type(request.json['service']) != str:
        abort(400)
    if 'version' in request.json and type(request.json['version']) != str:
        abort(400)
    if 'change' in request.json and type(request.json['change']) != str:
        abort(400)

    for i in range(0,len(service)):
        service[i]['service'] = request.json.get('service', service[i]['service'])
        service[i]['version'] = request.json.get('version', service[i]['version'])
        service[i]['change'] = u'changed'
        service[i]['change_version']=service[i]['change_version']+1

    return jsonify({'service': service})

#This is the delete end point
@app.route('/service_registry/api/v1.0/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = [service for service in services if service['id'] == service_id]
    if len(service) == 0:
        abort(404)
    services.remove(service[0])
    return jsonify({'sesrvice': service[0]['service'],'id': service[0]['id'],'change': 'removed'})
    services.append(service)
    return jsonify({'service': service}), 201
#This function is used to create a URI to our services. This helps the user interact with the service
#We have removed it for now and can be added in the future to help users make calls to services
#def make_public_service(service):
#    new_service = {}
#    for field in service:
#        if field == 'id':
#            new_service['uri'] = url_for('get_services', service_id=service['id'], _external=True)
#        else:
#            new_service[field] = service[field]
 #   return new_service

if __name__ == '__main__':
    app.run(debug=True)
