import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

email = 'user.name@gmail.com'
username = 'username'
password = 'password'

@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:

    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email=email, username=username, password=password)
        registration_page.registration_form.assert_visible(email=email, username=username, password=password)
        registration_page.click_register_button()
        dashboard_page.toolbar.assert_visible()
