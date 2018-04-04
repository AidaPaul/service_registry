# Created by Tymoteusz Paul at 18/01/2016
Feature: ServiceRegistry
Given an empty service registry
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


 
