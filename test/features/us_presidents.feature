Feature: DuckDuckGo Instant Answer API
  As a user,
  I want to be able to perform a query using the DuckDuckGo API for the "presidents of the united states"
  And get the list of each US Presidents

  Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo API is queried with "presidents of the united states"
    Then the response status code is "200"
    And the response contains the presidents listed in the RelatedTopics return field

  Scenario:  Basic DuckDuckGo Search
    Given the DuckDuckGo API is queried with "presidents of the united states"
    Then the response status code is "200"
    And I should be able to look for the last name of a president
