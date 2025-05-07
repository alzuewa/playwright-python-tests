from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent

from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.navbar = NavbarComponent(page=page)
        self.sidebar = SidebarComponent(page=page)

        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.students_chart_title = page.get_by_test_id('students-widget-title-text')
        self.students_chart = page.get_by_test_id('students-bar-chart')
        self.activities_chart_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_chart = page.get_by_test_id('activities-line-chart')
        self.courses_chart_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_chart = page.get_by_test_id('courses-pie-chart')
        self.scores_chart_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_chart = page.get_by_test_id('scores-scatter-chart')

    def assert_dashboard_title_visible(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')

    def assert_students_chart_visible(self):
        expect(self.students_chart).to_be_visible()
        expect(self.students_chart_title).to_be_visible()
        expect(self.students_chart_title).to_have_text('Students')

    def assert_activities_chart_visible(self):
        expect(self.activities_chart).to_be_visible()
        expect(self.activities_chart_title).to_be_visible()
        expect(self.activities_chart_title).to_have_text('Activities')

    def assert_courses_chart_visible(self):
        expect(self.courses_chart).to_be_visible()
        expect(self.courses_chart_title).to_be_visible()
        expect(self.courses_chart_title).to_have_text('Courses')

    def assert_scores_chart_visible(self):
        expect(self.scores_chart).to_be_visible()
        expect(self.scores_chart_title).to_be_visible()
        expect(self.scores_chart_title).to_have_text('Scores')
