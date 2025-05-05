from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context()
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

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_be_visible()
    empty_search_results_block = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_search_results_block).to_be_visible()
