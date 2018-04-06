Feature: service discovery
As a user of service_registry API, I like to be able to find services and get their counts back,
so that I can interact with the services and know their state and count

Background:
    Given add_Service_Registry is run
    and the following services exist:
      | service | version | change  | id  |
      | test    | 0.0.1   | created | 1   |
      | test    | 0.0.1   | created | 2   |
      | test    | 0.0.2   | created | 3   |
      | test    | 0.0.2   | created | 4   |
      | test2   | 0.0.2   | created | 5   |
      | test2   | 0.0.2   | created | 6   |


Scenario: Finding all services: only service name   
   When I search for a test service
      |test_service|
      |test|
   Then I should get a list of all the services
      | test    | 0.0.1   | created | id  |
      | test    | 0.0.1   | created |  1  |
      | test    | 0.0.2   | created |  2  |
      | test    | 0.0.2   | created |  3  |
      | test2   | 0.0.2   | created |  4  |
      | test2   | 0.0.2   | created |  5  |
   and the response should be paged 

 Scenario Outline: Finding all services with service and version
   When I search for a service/show_all "<service>" with version "<version>"
    Then I should find count "<count>" instances of service
    And the service "<service>" should have the correct type
    And the service "<service>" should have the correct version "<version>"
    Examples:
      | service | version | count |
      | test    | 0.0.1   |   2   |
      | test    | 0.0.2   |   2   |
      | test2   | 0.0.2   |   2   |

  Scenario Outline: Finding non existing service:
    When I search for a service "<service>" with version "<version>"
    Then I should find count "<count>" services
    Examples:
      | service | version | count |
      | test    | 0.0.4   |   0   |
      | test3   | 0.0.1   |   0   |


  Scenario Outline: Finding service without version:
    When I search for a service "<service>" without version
    Then I should find count "<count>" services
    And the service "<service>" should have the correct type
    Examples:
      | service | count |
      | test    |   4   |
      | test2   |   2   |
   
  Scenario Outline: Finding service unique id
    When I search for a service "<service>" with version "<version>" with number "<number>"
    Then I should get the uniqueID "<uniqueID>" of the service
    And the service "<service>" should have the correct type
    And the service "<service>" should have the correct version "<version>"
    Examples:
      | service | version | number| id|
      | test    | 0.0.1   | 1     | 1 |
      | test    | 0.0.1   | 2     | 2 |
      | test    | 0.0.2   | 1     | 3 |
      | test    | 0.0.2   | 2     | 4 |
      | test2   | 0.0.2   | 1     | 5 |
      | test2   | 0.0.2   | 2     | 6 |

  Scenario Outline: Finding service with non existing number:
    When I search for a service "<service>" with version "<version>" with number "<number>"
    Then I should find count "<count>" services
    Examples:

      | service | version | number| id                | count  |
      | test    | 0.0.1   | 3     | "No such service" |   0    | 
      | test    | 0.0.1   | b     | "No such service" |   0    |
      | test    | 0.0.2   | 3     | "No such service" |   0    |
      | test    | 0.0.2   | 10    | "No such service" |   0    |
      | test4   | 0.0.2   | 1     | "No such service" |   0    | 
      | test    | 0.0.4   | 1     | "No such service" |   0    |
