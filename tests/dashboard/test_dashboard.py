import pytest

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.dashboard
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_authorized: DashboardPage):
        dashboard_page_authorized.open(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        dashboard_page_authorized.navbar.assert_visible(username='username')
        dashboard_page_authorized.sidebar.assert_visible()

        dashboard_page_authorized.toolbar.assert_visible()
        dashboard_page_authorized.students_chart.assert_visible()
        dashboard_page_authorized.activities_chart.assert_visible()
        dashboard_page_authorized.courses_chart.assert_visible()
        dashboard_page_authorized.scores_chart.assert_visible()
