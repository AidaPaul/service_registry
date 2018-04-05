Feature: delete a service
As an API user, I want to be able to delete services, so that redundant services are removed and we don't get clutter.

Background:
   Given add_Service_Registry is run
    and the following services exist:
      | service | version | change  | uniqueID          | change_version |
      | test    | 0.0.1   | created | 0.0.1.1.epochtime |      1         |
      | test    | 0.0.1   | created | 0.0.1.2.epochtime |      1         |
      | test    | 0.0.2   | created | 0.0.2.1.epochtime |      2         |
      | test    | 0.0.2   | created | 0.0.2.2.epochtime |      1         |
      | test2   | 0.0.2   | created | 0.0.2.1.epochtime |      3         |
 
Scenario Outline: Removing a service:
    Given I call to remove a <service>
    When I remove the service
    Then the service should be removed
    And I should be notified with a change "<change>"
    
    Examples:
      | service | change |
      | test    | removed|
