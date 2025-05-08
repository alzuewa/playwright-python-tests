import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_authorized_state: DashboardPage):
    dashboard_page_authorized_state.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    dashboard_page_authorized_state.navbar.assert_visible(username='username')
    dashboard_page_authorized_state.sidebar.assert_visible()

    dashboard_page_authorized_state.assert_dashboard_title_visible()
    dashboard_page_authorized_state.assert_students_chart_visible()
    dashboard_page_authorized_state.assert_activities_chart_visible()
    dashboard_page_authorized_state.assert_courses_chart_visible()
    dashboard_page_authorized_state.assert_scores_chart_visible()
