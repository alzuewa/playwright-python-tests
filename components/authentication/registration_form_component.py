from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.email_field = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_field = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_field = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill_in_form(self, email: str, username: str, password: str):
        self.email_field.fill(email)
        expect(self.email_field).to_have_value(email)

        self.username_field.fill(username)
        expect(self.username_field).to_have_value(username)

        self.password_field.fill(password)
        expect(self.password_field).to_have_value(password)

    def assert_visible(self, email: str, username: str, password: str):
        expect(self.email_field).to_be_visible()
        expect(self.email_field).to_have_value(email)
        expect(self.username_field).to_be_visible()
        expect(self.username_field).to_have_value(username)
        expect(self.password_field).to_be_visible()
        expect(self.password_field).to_have_value(password)
