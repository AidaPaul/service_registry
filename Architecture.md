

- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  - [Install behave](#install-behave)


## Architecture
Reference-architecture
![reference architecture draft][logo]

[logo]: http://butlerthing.io/StudioH67/AWS_Architecture_ServiceRegistry.png "service registry architecture"

Thank you for the challenge, I did very much enjoy it.

+ We looked at the architecture and possible implementations.
+ We need to implement a BDD rest-assured like test framework.
+ There is further work on update functionality that is required.
+ User authentication should ideally be implemented.
+ Pagination for the calls should be implemented.
+ Lets discuss how we can use S3 as a consistent data base.
+ We need to add data base storgage and persistence to our code.
+ We think that there should be another test service that goes with service_register to test it.

## Installation
To install please clone the repo. Normally we recommend that you fork this repo and then clone it. However, if you havent forked it you can clone it using the following command.
`git clone https://github.com/ButlerThing/service_registry.git`

Let's begin by installing Flask in a virtual environment. If you don't have virtualenv installed in your system, you can download it from https://pypi.python.org/pypi/virtualenv.

```python
cd server_registry
pip install virtualenv
pip install flask
```
and to run the server:

```python
cd service-registery-api/
python service_resigter.py
```

Please run this command from the root folder of the repo once you have cloned it.

## Usage
from a different terminal run the following commands to interact with the API server:
```
curl -i http://localhost:5000/service_registry/api/v1.0/services 

curl -i http://localhost:5000/service_registry/api/v1.0/services/test     

curl -i -H "Content-Type: application/json" -X POST -d '{"service":"test","version":"1.0.3"}' http://localhost:5000/service_registry/api/v1.0/services

curl -i http://localhost:5000/service_registry/api/v1.0/services/test2   
```
### Install behave
pip3 install behave

```python
pip3 install -r requirements.txt
```
