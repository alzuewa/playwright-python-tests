from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.email_field = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_field = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_field = page.get_by_test_id('registration-form-password-input').locator('input')
        self.register_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def fill_in_registration_form(self, email: str, username: str, password: str):
        self.email_field.fill(email)
        expect(self.email_field).to_have_value(email)

        self.username_field.fill(username)
        expect(self.username_field).to_have_value(username)

        self.password_field.fill(password)
        expect(self.password_field).to_have_value(password)

        self.register_button.click()

    def click_login_link(self):
        self.login_link.click()
