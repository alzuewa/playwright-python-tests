import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Icon')
        self.title = Text(page, f'{identifier}-empty-view-title-text', 'Title')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Description')

    @allure.step('Check empty view "{title}" is visible')
    def assert_visible(self, title: str, description: str):
        self.icon.assert_visible()
        self.title.assert_visible()
        self.title.assert_have_text(text=title)
        self.description.assert_visible()
        self.description.assert_have_text(text=description)
