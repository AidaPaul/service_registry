Feature: update service status

As a user of service_registry API iwant to be able to update information about services,
so that desired changes are enabled on them and I have an up to date understanding of services
  
  Background:
      Given add_Service_Registry is run
    and the following services exist:
      | service | version | change  | id                | change_version |
      | test    | 0.0.1   | created | 1                 |      1         |
      | test    | 0.0.1   | created | 2                 |      1         |
      | test    | 0.0.2   | created | 3                 |      1         |
      | test    | 0.0.2   | created | 4                 |      1         |
      | test2   | 0.0.2   | created | 5                 |      1         |
      | test2   | 0.0.2   | created | 6                 |      1         |
  
  Scenario Outline: updating a service with service name only:
    When I update a <service>
    Then I should be notified with a change "<change>" and <change_version> should increment
    And update will happen to all services named <service>

    Examples:
     | service | change  | change_version |
     | test2   | changed |      2         |



  Scenario Outline: updating a service with service name and version:
    When I update a <service> and <version>
    Then I should be notified with a change "<change>" and <change_version> should increment to one higer than biggest <change_version> for this service and version combinaiton
    And update will happen to all services named <service> with version <version> only
    Examples:
      | service | version | change  |  change_version |
      | test    | 0.0.2   | changed |   2             |

      
      
   Scenario Outline: updating a service ID
   
    When I update a service with <id>
    Then I should be notified with a change "<change>" and <change_version> should increment to one higer than biggest <change_version> for this service and version combinaiton
    And update will happen one service only only
    And I should be notified with <service>
    Examples:
      | service | id      | change  |  change_version |
      | test    | 2       | changed |   3             |
