# Main test program. Still pretty basic stuff, but only been writing in python
# for 4 hours at this point :)
# Things I would improve - need to learn the libraries more and how python
# does its overloading, the multidispatch class I found is a little too basic.


from Service import *
from ServiceRegistry import *        

aService = Service("printer","0.0.1.1","original")
bService = Service("printer","0.0.1.1")

aServiceRegistry = ServiceRegistry()

#  Scenario Outline: Add service
#    When I add a service "<service>" with version "<version>"
#    Then I should be notified with a change "<change>"
#    Examples:
#      | service | version | change  |
      
print("TEST 1: ADD")
print("===========")
start_count = aServiceRegistry.size()
aServiceRegistry.add(aService)
if (aServiceRegistry.size() == start_count + 1):
    print ("test 1 success, service registry larger")
else:
    print ("test 1 failed, service registry not correct size")
    

#  Scenario Outline: Find service:
#    When I search for a service "<service>" with version "<version>"
#    Then I should find count "<count>" instances of service
#    And the service "<service>" should have the correct type
#    And the service "<service>" should have the correct version "<version>"
#    Examples:
#      | service | version | count |
#      | test    | 0.0.1   |   2   |

print("")
print("TEST 2: FIND")
print("============")
service_count = aServiceRegistry.find("printer","0.0.1.1")
print("")
if (aServiceRegistry.size() == start_count + 1):
    print ("test 2 success, service found")
else:
    print ("test 2 failed, service not found, but exists")


# add another printer of the same version
aServiceRegistry.add(bService)
if (aServiceRegistry.size() == start_count + 1):
    print ("test 2 success, service found")
else:
    print ("test 2 failed, service count doesn't match")
    
#  Scenario Outline: Finding non existing service:
#    When I search for a service "<service>" with version "<version>"
#    Then I should find count "<count>" services
#    Examples:
#      | service | version | count |
#      | test    | 0.0.4   |   0   |

print("")
print("TEST 3: FIND - no result")
print("========================")
service_count = aServiceRegistry.find("printer","0.0.3.1")
if (service_count == 0):
    print ("test 3 success, service should not be found")
else:
    print ("test 3 failed, service was found but doesn't exist")

#  Scenario Outline: Finding service without version:
#    When I search for a service "<service>" without version
#    Then I should find count "<count>" services
#    And the service "<service>" should have the correct type
#    Examples:
#      | service | count |
#      | test    |   4   |

print("")
cService = Service("printer","0.0.3.1")
aServiceRegistry.add(cService)

dService = Service("test","0.0.2.1","mutiple")
aServiceRegistry.add(dService)

service_count = aServiceRegistry.find("printer")
print("")
print("TEST 4: FIND on name only")
print("=========================")
service_count = len(aServiceRegistry.find("printer"))
if (service_count == 3):
    print ("test 4 success, 3 printer services")
else:
    print ("test 4 failed")

#  Scenario Outline: updating a service:
#    When I update a service
#    Then I should be notified with a change "<change>"
#    Examples:
#      | change  |
#      | changed |

aService = Service("upd_test","0.0.1.1","original")
aServiceRegistry.add(aService)

testSvcBefore = len(aServiceRegistry.find("upd_test","0.0.1.1"))
aService.set_version("0.1.0.0")
aServiceRegistry.update(aService)
aServiceRegistry.dump()
testSvcAfter = len(aServiceRegistry.find("upd_test","0.0.1.1"))
if (testSvcAfter == 0):
    print ("test 5 success, version updated")
else:
    print ("test 5 failed")
    
    
#  Scenario Outline: Removing a service:
#    When I remove a service
#    Then the service should be removed
#    And I should be notified with a change "<change>"
#    Examples:
#      | service | change |
#      | test    | removed|
aServiceRegistry.remove("printer")

print("")
print("TEST 6: REMOVE")
print("=========================")
service_count = len(aServiceRegistry.find("printer"))
if (service_count == 0):
    print ("test 6 success, no printer services found")
else:
    print ("test 6 failed")
    
#aServiceRegistry.update(bService)
#print(aServiceRegistry.count())
print("")
print("END: DUMP SERVICE REGISTRY")
print("==========================")
aServiceRegistry.dump()
