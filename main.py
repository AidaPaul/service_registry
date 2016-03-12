from service import Service

Service()
Service()
Service()

for service in Service.all_services:
	print(service)

