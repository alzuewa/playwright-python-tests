import re

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.routes import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with correct email or password')
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            dashboard_page: DashboardPage,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        registration_page.open(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_register_button()

        dashboard_page.toolbar.assert_visible()
        dashboard_page.navbar.assert_visible(username=settings.test_user.username)
        dashboard_page.sidebar.assert_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        dashboard_page.toolbar.assert_visible()
        dashboard_page.navbar.assert_visible(username=settings.test_user.username)
        dashboard_page.sidebar.assert_visible()

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with wrong email or password')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize(
        'email, password', [
            ('user.name@gmail.com', 'password'),
            ('user.name@gmail.com', '  '),
            ('  ', 'password')
        ]
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.open(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.assert_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.assert_wrong_creds_alert_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title('Navigation from login page to registration page')
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.open(AppRoute.LOGIN)
        login_page.click_registration_link()
        login_page.check_current_url(expected_url=re.compile(r'.*/#/auth/registration'))

        registration_page.registration_form.assert_visible(email='', username='', password='')
