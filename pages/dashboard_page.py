from playwright.sync_api import Page

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.navbar = NavbarComponent(page=page)
        self.sidebar = SidebarComponent(page=page)
        self.toolbar = DashboardToolbarViewComponent(page=page)
        self.students_chart = ChartViewComponent(page=page, identifier='students', char_type='bar', chart_name='Students')
        self.activities_chart = ChartViewComponent(page=page, identifier='activities', char_type='line', chart_name='Activities')
        self.courses_chart = ChartViewComponent(page=page, identifier='courses', char_type='pie', chart_name='Courses')
        self.scores_chart = ChartViewComponent(page=page, identifier='scores', char_type='scatter', chart_name='Scores')
