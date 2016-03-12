from service import Service, ServiceState
from exceptions import NoServiceWithId
from service_handler import ServiceHandler

def passed(function):
	print("+ " + function.__name__ + " passed")

def n_passed(function):
	print("\033[91m- " + function.__name__ + " did not passed!!\033[0m")


def add_service():
	if ServiceHandler.add_service("add_service", 0.1) == ServiceState.created:
		passed(add_service)
	else:
		n_passed(add_service)

def find_service1():
	ServiceHandler.add_service("find_service1", 0.1)
	ServiceHandler.add_service("find_service2", 0.1)
	ServiceHandler.add_service("find_service2", 0.1)
	if ServiceHandler.find_service("find_service2", 0.1) == 2:
		passed(find_service1)
	else:
		n_passed(find_service)

def find_service2():
	if ServiceHandler.find_service("blalblalbla", 0.1) == 0:
		passed(find_service2)
	else:
		n_passed(find_service2)

def find_service3():
	ServiceHandler.add_service("find_service1")
	ServiceHandler.add_service("find_service2", 0.1)
	ServiceHandler.add_service("find_service2", 0.1)
	if ServiceHandler.find_service("find_service1") == 1:
		passed(find_service3)
	else:
		n_passed(find_service3)

def update_service():
	if ServiceHandler.update_service(Service("update_service_test", 0.1), "updated_service") == ServiceState.changed:
		passed(update_service)
	else:
		n_passed(update_service)

def remove_service():
	if ServiceHandler.remove_service(Service("blabla", 0.2)) == ServiceState.removed:
		passed(remove_service)
	else:
		n_passed(remove_service)

if __name__ == '__main__':
	add_service()
	ServiceHandler.clear_all_services()
	find_service1()
	ServiceHandler.clear_all_services()
	find_service2()
	ServiceHandler.clear_all_services()
	find_service3()
	ServiceHandler.clear_all_services()
	update_service()
	ServiceHandler.clear_all_services()
	remove_service()
	ServiceHandler.clear_all_services()
