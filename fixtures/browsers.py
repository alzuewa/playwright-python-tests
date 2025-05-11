from pathlib import Path

import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    trace_report_path = Path(f'./traces/{request.node.name }.zip')
    context.tracing.stop(path=trace_report_path)
    browser.close()

    allure.attach.file(source=trace_report_path, name='playwright_trace', extension='zip')


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    chromium_browser = playwright.chromium.launch(headless=True)
    context = chromium_browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)

    registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_register_button()
    context.storage_state(path='browser-state.json')
    chromium_browser.close()


@pytest.fixture
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    chromium_browser = playwright.chromium.launch(headless=True)
    context = chromium_browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    trace_report_path = Path(f'./traces/{request.node.name}.zip')
    context.tracing.stop(path=trace_report_path)
    chromium_browser.close()

    allure.attach.file(source=trace_report_path, name='playwright_trace', extension='zip')
