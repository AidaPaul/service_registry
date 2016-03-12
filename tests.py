from service import Service, ServiceState
from exceptions import NoServiceWithId

def passed(function):
	print("+ " + function.__name__ + " passed")

def n_passed(function):
	print("- " + function.__name__ + " not passed!!")

def constructor_test():
	myService = Service("test1", 0.1)
	if myService.service_name == "test1" and myService.initial_version == 0.1:
		passed(constructor_test)
	else:
		n_passed(constructor_test)

def update_service_name():
	myService = Service("test1", 0.1)
	Service.update_service(myService, new_service_name = "test2") ## updating name
	if myService.service_name == "test2" and myService.current_version == 0.1 and myService.state == ServiceState.changed:
		passed(update_service_name)
	else:
		n_passed(update_service_name)

def update_service_version():
	myService = Service("test1", 0.1)
	Service.update_service(myService, new_service_version = 0.2) ## updating name
	if myService.service_name == "test1" and myService.current_version == 0.2 and myService.state == ServiceState.changed:
		passed(update_service_name)
	else:
		n_passed(update_service_name)

def exception_test():
	try:
		Service.get_service_by_id(40)
	except NoServiceWithId:
		passed(exception_test)
		return
	n_passed(exception_test)

constructor_test()
exception_test()
update_service_name()
update_service_version()