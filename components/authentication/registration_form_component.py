from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.email_field = Input(page, 'registration-form-email-input', 'Email')
        self.username_field = Input(page, 'registration-form-username-input', 'Username')
        self.password_field = Input(page, 'registration-form-password-input', 'Password')

    def fill(self, email: str, username: str, password: str):
        self.email_field.fill(value=email)
        self.email_field.assert_have_value(value=email)
        self.username_field.fill(value=username)
        self.username_field.assert_have_value(value=username)
        self.password_field.fill(value=password)
        self.password_field.assert_have_value(value=password)

    def assert_visible(self, email: str, username: str, password: str):
        self.email_field.assert_visible()
        self.email_field.assert_have_value(value=email)
        self.username_field.assert_visible()
        self.username_field.assert_have_value(value=username)
        self.password_field.assert_visible()
        self.password_field.assert_have_value(value=password)
