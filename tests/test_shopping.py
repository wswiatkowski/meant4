import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/shopping_flow.feature')


@given('I open White Blouse product page')
def open_white_blouse_product(page):
    page.goto("http://www.automationpractice.pl/index.php?id_product=2&controller=product#/1-size-s/8-color-white")


@given('I add product to cart')
def add_product_to_cart(page):
    page.get_by_text('Add to cart').click()


@given('I proceed')
def proceed_to_checkout(page):
    page.get_by_text('Proceed to checkout').last.click()


@given('I agree to terms of service')
def agree_to_terms_of_service(page):
    page.check('input[name="cgv"]')


@when('I select bank wire payment')
def select_bank_wire_payment(page):
    page.get_by_text('Pay by bank wire').click()


@when('I confirm my order')
def confirm_order(page):
    page.get_by_text('I confirm my order').last.click()




