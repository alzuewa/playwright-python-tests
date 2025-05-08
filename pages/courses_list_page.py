from playwright.sync_api import Page

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.navbar = NavbarComponent(page=page)
        self.sidebar = SidebarComponent(page=page)
        self.toolbar = CoursesListToolbarViewComponent(page=page, identifier='courses-list', title_text='Courses')
        self.course_view = CourseViewComponent(page=page)
        self.courses_empty_view = EmptyViewComponent(
            page=page,
            identifier='courses-list',
            title_text='There is no results',
            description_text='Results from the load test pipeline will be displayed here'
        )

    def assert_empty_view_visible(self):
        self.courses_empty_view.assert_visible()
