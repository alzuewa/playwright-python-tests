import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.dashboard_list_item = SidebarListItemComponent(page=page, identifier='dashboard')
        self.courses_list_item = SidebarListItemComponent(page=page, identifier='courses')
        self.logout_list_item = SidebarListItemComponent(page=page, identifier='logout')

    def assert_visible(self):
        self.dashboard_list_item.assert_visible(item_title='Dashboard')
        self.courses_list_item.assert_visible(item_title='Courses')
        self.logout_list_item.assert_visible(item_title='Logout')

    def click_logout(self):
        self.logout_list_item.navigate(expected_url=re.compile(r'.*/#/auth/login'))

    def click_courses(self):
        self.courses_list_item.navigate(expected_url=re.compile(r'.*/#/courses'))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(expected_url=re.compile(r'.*/#/dashboard'))
