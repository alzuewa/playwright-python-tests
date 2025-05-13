import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
from utils.routes import AppRoute


class SidebarComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.dashboard_list_item = SidebarListItemComponent(page=page, identifier='dashboard')
        self.courses_list_item = SidebarListItemComponent(page=page, identifier='courses')
        self.logout_list_item = SidebarListItemComponent(page=page, identifier='logout')

    @allure.step('Check sidebar is visible')
    def assert_visible(self):
        self.dashboard_list_item.assert_visible(item_title='Dashboard')
        self.courses_list_item.assert_visible(item_title='Courses')
        self.logout_list_item.assert_visible(item_title='Logout')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(expected_url=re.compile(r'.*/#/auth/login'))

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(expected_url=re.compile(r'.*/#/courses'))

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(expected_url=re.compile(r'.*/#/dashboard'))
