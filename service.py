from exceptions import NoServiceWithId

class ServiceState:
	unchanged = 0
	changed = 1
	created = 3
	removed = 4

class Service(object):

	all_services = []
	latest_id = 0

	def __init__(self, service_name="noname", version=None):
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
		self.service_name = new_name		

	def register(self):
		Service.all_services.append(self)

	def change_state(self):
		if self.state == ServiceState.unchanged:
			self.state = ServiceState.changed
		else:
			self.state = ServiceState.unchanged

	def __str__(self):
		return "name: " + self.service_name + " id: " + str(self.id)

	@staticmethod
	def get_service_by_id(id):
		for service in Service.all_services:
			if service.id == id:
				return service
		raise NoServiceWithId("there is no service with provided id")

	@staticmethod
	def find_service_by_name(name):
		found_services_count = 0
		for service in Service.all_services:
			if service.service_name == name:
				found_services_count += 1
		return found_services_count

	@staticmethod
	def find_service(name, version):
		found_services_count = 0
		for service in Service.all_services:
			if service.service_name == name and service.current_version == version:
				found_services_count += 1
		return found_services_count

	@staticmethod
	def update_service(service_to_update, new_service_name=None, new_service_version=None):
		if new_service_name is not None and new_service_version is None:
			service_to_update.update_service_name(new_service_name)
			service_to_update.change_state()
			return service_to_update.state
		elif new_service_name is None and new_service_version is not None:
			service_to_update.update_service_version(new_service_version)
			service_to_update.change_state()
			return service_to_update.state
		elif new_service_name is not None and new_service_version is not None:
			service_to_update.update_service_name(new_service_name)
			service_to_update.update_service_version(new_service_version)
			service_to_update.change_state()
			return service_to_update.state

	@staticmethod
	def remove_service(service):
		Service.all_services.remove(service)
		return ServiceState.removed
