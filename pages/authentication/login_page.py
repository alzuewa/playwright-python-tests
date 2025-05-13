import re

import allure
from playwright.sync_api import Page

from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from utils.routes import AppRoute


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page=page)
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.register_link = Link(page, 'login-page-registration-link', 'Registration')
        self.wrong_creds_alert = Text(
            page, 'login-page-wrong-email-or-password-alert', 'Wrong email or password'
        )

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.register_link.click()
        self.check_current_url(expected_url=re.compile(fr'.*{AppRoute.REGISTRATION}'))

    @allure.step('Check visible wrong email or password alert')
    def assert_wrong_creds_alert_visible(self):
        self.wrong_creds_alert.assert_visible()
        self.wrong_creds_alert.assert_have_text(text='Wrong email or password')
