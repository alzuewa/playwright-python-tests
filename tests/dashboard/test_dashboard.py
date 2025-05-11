import allure
import pytest
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from utils.allure_strings.epics import AllureEpic
from utils.allure_strings.features import AllureFeature
from utils.allure_strings.stories import AllureStory
from utils.allure_strings.tags import AllureTag


@pytest.mark.regression
@pytest.mark.dashboard
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:

    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
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
