import pytest
import allure

from playwright.sync_api import sync_playwright
from pytest_bdd import scenarios, given, when, then, parsers
from allure_commons.types import AttachmentType


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


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    page = request.getfixturevalue('page')
    page.wait_for_load_state('networkidle')
    screenshot = page.screenshot()
    allure.attach(
        body=screenshot,
        name=f'screenshot_{step.name}',
        attachment_type=AttachmentType.PNG
    )


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