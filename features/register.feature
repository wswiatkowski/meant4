Feature: Register new User to My Shop

  Scenario Outline: Register new user (negative)
    Given I open shop Main Page
    And I click on Sign in button
    And I create an account with email "user1@internet.com"
    When I fill in personal information with "<title>", "<first_name>", "<last_name>"
    And I continue filling in with "<password>", "<dob_day>", "<dob_month>", "<dob_year>", "<newsletter>"
    And I click on Register button
    Then I should see "<error_message>" text

    Examples:
      | title | first_name | last_name | password | dob_day | dob_month | dob_year | newsletter | error_message          |
      | Mr    | 0          | Doe       | password | 1       | 1         | 2000     | yes        | firstname is invalid.  |
      | Mrs   | Jane       | 0         | password | 1       | 2         | 2000     | yes        | lastname is invalid.   |
      | Ms    | Alice      | Doe       | 0        | 1       | 3         | 2000     | yes        | passwd is invalid.     |
      | Mr    | null       | Doe       | password | 1       | 4         | 2000     | yes        | firstname is required. |
      | Mrs   | Jane       | null      | password | 1       | 5         | 2000     | yes        | lastname is required.  |
      | Ms    | Alice      | Doe       | null     | 1       | 6         | 2000     | yes        | passwd is required.    |


  Scenario: Register new user (positive)
    Given I open shop Main Page
    And I click on Sign in button
    And I create an account with email "random"
    When I fill in personal information with "Mrs", "Anna", "Doe"
    And I continue filling in with "1234567", "19", "3", "1995", "yes"
    And I click on Register button
    Then I should see " Your account has been created." text
    And I logout
