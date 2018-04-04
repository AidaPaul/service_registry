  Scenario Outline: updating a service:
    When I update a service
    Then I should be notified with a change "<change>"
    Examples:
      | change  |
      | changed |
