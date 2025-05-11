import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.email_field = Input(page, 'login-form-email-input', 'Email')
        self.password_field = Input(page, 'login-form-password-input', 'Password')

    @allure.step('Fill in login form')
    def fill(self, email: str, password: str):
        self.email_field.fill(value=email)
        self.email_field.assert_have_value(value=email)
        self.password_field.fill(value=password)
        self.password_field.assert_have_value(value=password)

    @allure.step('Check login form is visible')
    def assert_visible(self, email: str, password: str):
        self.email_field.assert_visible()
        self.email_field.assert_have_value(value=email)
        self.password_field.assert_visible()
        self.password_field.assert_have_value(value=password)
