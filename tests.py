from service import Service

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

constructor_test()