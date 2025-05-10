import allure
import pytest
from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.suites import AllureParentSuite, AllureSuite, AllureSubSuite
from utils.allure.tags import AllureTag

email = 'user.name@gmail.com'
username = 'username'
password = 'password'


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.REGISTRATION)
class TestRegistration:

    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email=email, username=username, password=password)
        registration_page.registration_form.assert_visible(email=email, username=username, password=password)
        registration_page.click_register_button()
        dashboard_page.toolbar.assert_visible()
