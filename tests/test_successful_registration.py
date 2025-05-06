from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_in_registration_form(
        email='user.name@gmail.com',
        username='username',
        password='password'
    )
    dashboard_page.assert_dashboard_title_visible()
