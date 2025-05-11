import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step('Check dashboard toolbar is visible')
    def assert_visible(self):
        self.title.assert_visible()
        self.title.assert_have_text(text='Dashboard')
