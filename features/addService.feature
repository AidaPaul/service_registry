# Created by Tymoteusz Paul at 18/01/2016
Feature: ServiceRegistry add service
Given an empty service registry
  Scenario Outline: Add service
    When I add a service "<service>" with version "<version>"
    Then I should be notified with a change "<change> and a unique service identifier <uniqueID>"
    Examples:
      | service | version | change  | uniqueID          |
      | test    | 0.0.1   | created | 0.0.1.1.epochtime |
      | test    | 0.0.1   | created | 0.0.1.2.epochtime |
      | test    | 0.0.2   | created | 0.0.2.1.epochtime |
      | test    | 0.0.2   | created | 0.0.2.2.epochtime |
      | test2   | 0.0.2   | created | 0.0.2.1.epochtime |
      | test2   | 0.0.2   | created | 0.0.2.2.epochtime |


 
