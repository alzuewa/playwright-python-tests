import pytest
from playwright.sync_api import Page

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    login_page = LoginPage(page=chromium_page)
    return login_page


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    registration_page = RegistrationPage(page=chromium_page)
    return registration_page


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    dashboard_page = DashboardPage(page=chromium_page)
    return dashboard_page
