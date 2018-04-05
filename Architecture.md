
Reference-architecture: 
![reference architecture draft][logo]

[logo]: http://butlerthing.io/StudioH67/AWS_Architecture_ServiceRegistry.png "service registry architecture"

Thank you for the challenge, I did very much enjoy it.
We looked at the architecture and possible implementations.
We need to implement a BDD rest-assured like test framework.
There are vaious bugs in my post code that needs resovling
Lets discuss how we can use S3 as a consistent data base
We need to add data base storgage and persistence to our code
We think that there should be another test service that goes with service_register to test it.

To install please cloen or repo.

py -m pip --version

py -m pip install --upgrade pip

run pip install -r requirements.txt

pip install virtualenv

flask/bin/pip install flask

and to run the server:
python service_resigter.py

Please run this command fro the route folder of the repo once you have cloned it.
 from a different terminal run the following commands to interact with the API server:
 
curl -i http://localhost:5000/service_registry/api/v1.0/findServices/test     

curl -i -H "Content-Type: application/json" -X POST -d '{"service":"test"}' http://localhost:5000/service_registry/api/v1.0/addService

curl -i http://localhost:5000/service_registry/api/v1.0/findServices/test2   
