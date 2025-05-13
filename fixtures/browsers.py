import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config import settings
from pages.authentication.registration_page import RegistrationPage
from utils.playwright.pages import initialize_playwright_page
from utils.routes import AppRoute


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    chromium_browser = playwright.chromium.launch(headless=True)
    context = chromium_browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)

    registration_page.open(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.click_register_button()
    context.storage_state(path=settings.browser_state_file)
    chromium_browser.close()


@pytest.fixture
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )
