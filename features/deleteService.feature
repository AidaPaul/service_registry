Feature: delete a service
Scenario Outline: Removing a service:
    When I remove a service
    Then the service should be removed
    And I should be notified with a change "<change>"
    Examples:
      | service | change |
      | test    | removed|
