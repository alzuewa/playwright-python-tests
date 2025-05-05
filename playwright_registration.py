from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_field = page.locator('[data-testid="registration-form-email-input"] input')
    email_field.fill('user.name@gmail.com')
    username_field = page.locator('[data-testid="registration-form-username-input"] input')
    username_field.fill('username')
    password_field = page.locator('[data-testid="registration-form-password-input"] input')
    password_field.fill('password')
    password_field.click()

    register_button = page.locator('[data-testid="registration-page-registration-button"]')
    register_button.click()

    dashboard_header = page.locator('[data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard_header).to_be_visible()
