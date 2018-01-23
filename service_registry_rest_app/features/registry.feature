# Created by Tymoteusz Paul at 18/01/2016
Feature: ServiceRegistry

  Background:
    Given there is an empty ServiceRegistry

  Scenario Outline: Add service
    When I add a service "<service>" with version "<version>"
    Then I should be notified with a change "<change>"
    Examples:
      | service | version | change  |
      | test    | 0.0.1   | created |
      | test    | 0.0.1   | created |
      | test    | 0.0.2   | created |
      | test    | 0.0.2   | created |
      | test2   | 0.0.2   | created |
      | test2   | 0.0.2   | created |


  Scenario Outline: Find service:
    When I search for a service "<service>" with version "<version>"
    Then I should find count "<count>" instances of service
    Examples:
      | service | version | count |
      | test    | 0.0.1   |   2   |
      | test    | 0.0.2   |   2   |
      | test2   | 0.0.2   |   2   |

