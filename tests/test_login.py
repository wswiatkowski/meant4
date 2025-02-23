import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/login.feature')


@then('I should see My account page')
def should_see_my_account_page(page):
    page.wait_for_load_state('networkidle')
    assert page.title() == "My account - My Shop"
