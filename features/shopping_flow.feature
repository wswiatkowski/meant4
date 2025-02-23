Feature: Shopping Flow

  Scenario: Add product to cart
    Given I open shop Main Page
    And I click on Sign in button
    And I log in with email "email@internet.pl" and password "123456"
    And I open White Blouse product page
    And I add product to cart
    And I should see "There is 1 item in your cart." text
    And I proceed
    And I should see "Your shopping cart contains: 1 Product" text
    And I proceed
    And I should see "Your billing address" text
    And I proceed
    And I should see "Choose a shipping option for this address: My address" text
    And I agree to terms of service
    And I proceed
    When I select bank wire payment
    And I should see "You have chosen to pay by bank wire." text
    And I confirm my order
    Then I should see "Your order on My Shop is complete." text
    And I logout

