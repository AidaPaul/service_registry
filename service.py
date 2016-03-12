from exceptions import NoServiceWithId

class ServiceState:
	unchanged = 0
	changed = 1

class Service(object):

	all_services = []
	latest_id = 0

	def __init__(self, service_name, version):
		self.service_name = service_name
		self.initial_version = version
		self.current_version = version
		self.state = ServiceState.unchanged
		self.id = Service.latest_id + 1
		Service.latest_id += 1 
		self.register()

	def update_service_version(self, new_version):
		self.current_version = new_version

	def update_service_name(self, new_name):
		self.name = new_name		

	def register(self):
		Service.all_services.append(self)

	def change_state(self):
		if self.state == ServiceState.unchanged:
			self.state = ServiceState.changed
		else:
			self.state = ServiceState.unchanged

	@staticmethod
	def get_service_by_id(id):
		for service in Service.all_services:
			if service.id == id:
				return service
		raise NoServiceWithId("there is no service with provided id")

	@staticmethod
	def update_service(service_to_update, new_service_name=None, new_service_version=None):
		if new_service_name is not None and new_service_version is None:
			service_to_update.update_service_name(new_service_name)
			service_to_update.change_state()
		elif new_service_name is None and new_service_version is not None:
			service_to_update.update_service_version(new_service_version)
			service_to_update.change_state()
		elif new_service_name is not None and new_service_version is not None:
			service_to_update.update_service_name(new_service_name)
			service_to_update.update_service_version(new_service_version)
			service_to_update.change_state()
