from typing import Pattern

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Sidebar item icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Sidebar item title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Sidebar item button')

    @allure.step('Check "{item_title}" sidebar list item is visible')
    def assert_visible(self, item_title: str):
        self.icon.assert_visible()
        self.title.assert_visible()
        self.title.assert_have_text(text=item_title)
        self.button.assert_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url=expected_url)
