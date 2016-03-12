from service import Service
from exceptions import NoServiceWithId
from service import ServiceState

class ServiceHandler:

	def add_service(service_name, service_version=None):
		Service(service_name, service_version)
		return ServiceState.created

	def remove_service(service):
		return Service.remove_service(service)

	def find_service(name, version=None):
		if version is None:
			return Service.find_service_by_name(name)
		else:
			return Service.find_service(name, version)
		return 0

	def update_service(service_to_update, new_service_name=None, new_service_version=None):
		return Service.update_service(service_to_update, new_service_name, new_service_version)

	def clear_all_services():
		Service.all_services = []
