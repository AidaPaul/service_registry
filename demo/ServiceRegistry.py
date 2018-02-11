from Service import *
from multidispatch import *
from itertools import filterfalse

# Stole base pattern from somewhere on the web :)
class ServiceRegistry:
    """ A python singleton """
    _services = []
    

    class __impl:
        """ Implementation of the singleton interface """

        def spam(self):
            """ Test method, return singleton id """
            return id(self)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if ServiceRegistry.__instance is None:
            # Create and remember instance
            ServiceRegistry.__instance = ServiceRegistry.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_ServiceRegistry__instance'] = ServiceRegistry.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)


    # New methods to fulfil the requirements
    def size(self):
        return(len(ServiceRegistry._services))

    def add(self,service):
        ServiceRegistry._services.append(service)
        self.notify("add",service)

    def update(self,service):
        i = ServiceRegistry._services.index(service)
        ServiceRegistry._services[i] = service
        self.notify_all("changed",service.name())

    def remove(self,name):     
        self._services[:] = [service for service in self._services if not(service.name_match(name))]
        self.notify_all("removed", name)

    @multidispatch(str,str)
    def find(self, name, version):
        _results = []
        for service in self._services:
            if (service.name() == name and service.version() == version):
                _results.append(service)
        print("| {n:15s} | {v:10s} | {c:5s} |".format(n="service", v="version",c="count"))
        print("| {n:15s} | {v:10s} | {c:5d} |".format(n=name, v=version,c=len(_results)))
        return _results
       
    @multidispatch(str)
    def find(self, name):
        _results = []
        for service in self._services:
            if (service.name() == name):
                _results.append(service)
        print("| {n:15s} | {c:5s} |".format(n="service", c="count"))
        print("| {n:15s} | {c:5d} |".format(n=name, c=len(_results)))
        return _results

    #tbd: really need to shove all these prints into overloaded methods
    def notify_all(self, action, name):
        print("| {n:15s} | {a:10s} |".format(n="service", a="change"))
        print("| {n:15s} | {a:10s} |".format(n=name, a=action))
        
    def notify(self, action, service):
        print("| {n:15s} | {v:10s} | {a:10s} |".format(n="service", v="version",a="change"))
        print("| {n:15s} | {v:10s} | {a:10s} |".format(n=service.name(), v=service.version(),a=action))

    def dump(self):
        print("There are {c:5d} services in the registry".format(c=self.size()))
        for service in self._services:
            service.dump()
