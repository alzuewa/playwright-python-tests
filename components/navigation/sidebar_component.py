import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.dashboard_list_item = SidebarListItemComponent(page=page, identifier='dashboard', item_name='Dashboard')
        self.courses_list_item = SidebarListItemComponent(page=page, identifier='courses', item_name='Courses')
        self.logout_list_item = SidebarListItemComponent(page=page, identifier='logout', item_name='Logout')

    def assert_visible(self):
        self.dashboard_list_item.assert_visible()
        self.courses_list_item.assert_visible()
        self.logout_list_item.assert_visible()

    def click_logout(self):
        self.logout_list_item.navigate(expected_url=re.compile(r'.*/#/auth/login'))

    def click_courses(self):
        self.courses_list_item.navigate(expected_url=re.compile(r'.*/#/courses'))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(expected_url=re.compile(r'.*/#/dashboard'))
