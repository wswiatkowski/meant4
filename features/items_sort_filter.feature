Feature: Items Sorting and Filtering

  Scenario: Select all filters
    Given I open shop Main Page
    And I open "woman" products category
    When I check all filters
    Then Page url should contain all selected filters

  Scenario Outline: Select products sorting
    Given I open shop Main Page
    And I open "woman" products category
    When I select sorting option "<sorting>"
    Then Page url should contain "<ordering>" text

    Examples:
    | sorting         | ordering                        |
    | price:asc       | orderby=price&orderway=asc      |
    | price:desc      | orderby=price&orderway=desc     |
    | name:asc        | orderby=name&orderway=asc       |
    | name:desc       | orderby=name&orderway=desc      |
    | quantity:desc   | orderby=quantity&orderway=desc  |
    | reference:asc   | orderby=reference&orderway=asc  |
    | reference:desc  | orderby=reference&orderway=desc |