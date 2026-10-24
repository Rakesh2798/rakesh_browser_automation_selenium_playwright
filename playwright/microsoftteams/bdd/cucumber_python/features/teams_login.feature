Feature: Microsoft Teams sign-in page
  As a Teams user
  I want to sign in
  So that I can use Teams

  Scenario: User signs in to Microsoft Teams
    Given I provide my Teams email and password
    When I sign in to Microsoft Teams
    Then the Teams home page is displayed
