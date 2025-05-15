from playwright.sync_api import sync_playwright, expect

from config import settings
from utils.routes import AppRoute

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=settings.headless)
    context = chromium.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_field = page.locator('[data-testid="registration-form-email-input"] input')
    email_field.fill(settings.test_user.email)
    username_field = page.locator('[data-testid="registration-form-username-input"] input')
    username_field.fill(settings.test_user.username)
    password_field = page.locator('[data-testid="registration-form-password-input"] input')
    password_field.fill(settings.test_user.password)
    password_field.click()

    register_button = page.locator('[data-testid="registration-page-registration-button"]')
    register_button.click()

    dashboard_header = page.locator('[data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard_header).to_be_visible()
