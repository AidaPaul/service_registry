# Let's write: service registry

## Overview ([Task source](https://github.com/Puciek/service_registry))
This service is responsible of keeping track of services within the system. It is a restful way for services to find other services, ensure that they are healthy.

## Further development notes
- there could be email notification (asynchronous) in some cases like new service has been added (it would use celery or spawn new thread) or service health check (also async)
- there could be some kind of authorization
- there could be one update_service function which would update any field in the database
- there could be a config file with settings such as port, loglevel
- not_empty_str validator could also be checking for invalid characters and string max length, simply in a loop or with regexp but then it should also check for input length for regexp security


