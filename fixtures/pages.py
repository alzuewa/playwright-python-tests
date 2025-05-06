import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    login_page = LoginPage(page=chromium_page)
    return login_page
