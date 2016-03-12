from service import Service
from exceptions import NoServiceWithId

class ServiceHandler:

	def add_service(service_name, service_version):
		Service(service_name, service_version)

	def remove_service(service):
		Service.remove_service(Service.get_service_by_id(id))

	def find_service(name, version=None):
		if version is None:
			return Service.find_service_by_name(name)
		else:
			return Service.find_service(name, version)

	def update_service(service_to_update, new_service_name=None, new_service_version=None)
		Service.update_service(service_to_update, new_service_name, new_service_version)