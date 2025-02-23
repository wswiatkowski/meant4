import pytest
from pytest_bdd import scenarios, given, when, then, parsers

import datetime

scenarios('../features/register.feature')


@given(parsers.parse('I create an account with email "{email}"'))
@when(parsers.parse('I create an account with email "{email}"'))
def create_account(page, email):
    page.fill('input[name="email_create"]', email if email != 'random' else f"test{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}@test.com")
    page.click('button[id="SubmitCreate"]')


@when(parsers.parse('I fill in personal information with "{title}", "{first_name}", "{last_name}"'))
def fill_in_personal_information(page, title, first_name, last_name):
    page.click('input[id="id_gender2"]' if title == "Mrs" else 'input[id="id_gender1"]')
    page.fill('input[name="customer_firstname"]', first_name if first_name != "null" else "")
    page.fill('input[name="customer_lastname"]', last_name if last_name != "null" else "")


@when(parsers.parse('I continue filling in with "{password}", "{dob_day}", "{dob_month}", "{dob_year}", "{newsletter}"'))
def continue_with(page, password, dob_day, dob_month, dob_year, newsletter):
    page.fill('input[name="passwd"]', password if password != "null" else "")
    page.select_option('select[name="days"]', dob_day)
    page.select_option('select[name="months"]', dob_month)
    page.select_option('select[name="years"]', dob_year)
    if newsletter == "yes":
        page.check('input[name="newsletter"]')
    else:
        page.uncheck('input[name="newsletter"]')


@when('I click on Register button')
def click_on_register_button(page):
    page.wait_for_load_state('networkidle')
    page.get_by_text('Register').click()
