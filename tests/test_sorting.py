import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/items_sort_filter.feature')


@given('I open "woman" products category')
def woman_products_category(page):
    page.click('a[title="Women"]')


@when('I check all filters')
def check_filters(page):
    for checkbox in page.locator("input[type='checkbox']").all():
        checkbox.check()


@then("Page url should contain all selected filters")
def check_filters(page):
    page.wait_for_url('http://www.automationpractice.pl/index.php?id_category=3&controller=category#/'
                      'categories-tops-dresses/size-s-m-l/properties-colorful_dress-maxi_dress-midi_'
                      'dress-short_dress-short_sleeve/compositions-cotton-polyester-viscose/styles-'
                      'casual-dressy-girly/availability-not_available-in_stock/condition-new')

    assert ("id_category=3&controller=category#/categories-tops-dresses/size-s-m-l/properties-"
            "colorful_dress-maxi_dress-midi_dress-short_dress-short_sleeve/compositions-cotton-"
            "polyester-viscose/styles-casual-dressy-girly/availability-not_available-in_stock/condition-new") in page.url


@when(parsers.parse('I select sorting option "{sorting}"'))
def select_sorting(page, sorting):
    page.select_option('select[id="selectProductSort"]', sorting)


@then(parsers.parse('Page url should contain "{text}" text'))
def check_text(page, text):
    page.wait_for_load_state('networkidle')
    assert text in page.url
