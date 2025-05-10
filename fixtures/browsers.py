import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    chromium_browser = playwright.chromium.launch(headless=True)
    context = chromium_browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill('user.name@gmail.com')
    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    username_field.fill('username')
    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill('password')
    password_field.click()

    register_button = page.get_by_test_id('registration-page-registration-button')
    register_button.click()

    context.storage_state(path='browser-state.json')
    chromium_browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    chromium_browser = playwright.chromium.launch(headless=True)
    context = chromium_browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    yield page

    chromium_browser.close()
