from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_field = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_field = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.register_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_creds_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def fill_in_login_form(self, email: str, password: str):
        self.email_field.fill(email)
        expect(self.email_field).to_have_value(email)

        self.password_field.fill(password)
        expect(self.password_field).to_have_value(password)

        self.login_button.click()

    def click_registration_link(self):
        self.register_link.click()

    def assert_wrong_creds_alert_visible(self):
        expect(self.wrong_creds_alert).to_be_visible()
        expect(self.wrong_creds_alert).to_have_text('Wrong email or password')
