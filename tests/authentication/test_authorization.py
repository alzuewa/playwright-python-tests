import re

import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:

    def test_successful_authorization(
            self,
            dashboard_page: DashboardPage,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
        registration_page.click_register_button()

        dashboard_page.toolbar.assert_visible()
        dashboard_page.navbar.assert_visible(username='username')
        dashboard_page.sidebar.assert_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='user.name@gmail.com', password='password')
        login_page.click_login_button()

        dashboard_page.toolbar.assert_visible()
        dashboard_page.navbar.assert_visible(username='username')
        dashboard_page.sidebar.assert_visible()

    @pytest.mark.parametrize(
        'email, password', [
            ('user.name@gmail.com', 'password'),
            ('user.name@gmail.com', '  '),
            ('  ', 'password')
        ]
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.assert_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.assert_wrong_creds_alert_visible()

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()
        login_page.check_current_url(expected_url=re.compile('.*/#/auth/registration'))

        registration_page.registration_form.assert_visible(email='', username='', password='')
