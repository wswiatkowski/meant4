import pytest
from playwright.sync_api import sync_playwright
from pytest_bdd import scenarios, given, when, then, parsers


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()


@given('I open shop Main Page')
def open_shop_main_page(page):
    page.goto("http://automationpractice.pl")


@given('I click on Sign in button')
def click_on_sign_in_button(page):
    page.click('text=Sign in')


@given(parsers.parse('I log in with email "{email}" and password "{password}"'))
def login(page, email, password):
    page.fill('input[name="email"]', email)
    page.fill('input[name="passwd"]', password)
    page.click('button[id="SubmitLogin"]')


@given(parsers.parse('I should see "{text}" text'))
@when(parsers.parse('I should see "{text}" text'))
@then(parsers.parse('I should see "{text}" text'))
def should_see_text(page, text):
    page.wait_for_timeout(777)
    elem = page.get_by_text(text)
    assert elem.is_visible()


@then('I logout')
def logout(page):
    page.click('text=Sign out')