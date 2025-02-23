Feature: Login to My Shop

  Scenario Outline: Log into My Shop (negative)
    Given I open shop Main Page
    And I click on Sign in button
    And I log in with email "<email>" and password "<password>"
    Then I should see "<error_message>" text

    Examples:
      | email             | password | error_message          |
      | bad@email.com     | 1        | Invalid password.      |
      | wrongemail.com    | password | Invalid email address. |
      | email@com         | password | Invalid email address. |
      | email@internet.pl | p@ssw0rd | Authentication failed. |

  Scenario: Log into My Shop (positive)
    Given I open shop Main Page
    And I click on Sign in button
    And I log in with email "email@internet.pl" and password "123456"
    Then I should see My account page
    And I logout