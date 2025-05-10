import pytest

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_authorized_state: DashboardPage):
    dashboard_page_authorized_state.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    dashboard_page_authorized_state.navbar.assert_visible(username='username')
    dashboard_page_authorized_state.sidebar.assert_visible()

    dashboard_page_authorized_state.toolbar.assert_visible()
    dashboard_page_authorized_state.students_chart.assert_visible()
    dashboard_page_authorized_state.activities_chart.assert_visible()
    dashboard_page_authorized_state.courses_chart.assert_visible()
    dashboard_page_authorized_state.scores_chart.assert_visible()
