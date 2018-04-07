Feature: delete a service
As an API user, I want to be able to delete services, so that redundant services are removed and we don't get clutter.
 
Scenario Outline: Removing a service:
    Given service_registry is run
    And I call to remove a service with <id>
    When I remove the service
    Then the service should be removed
    And I should be notified with a change "<change>"
    
    Examples:
      | service | id  | change |
      | test    |  1  | removed|
