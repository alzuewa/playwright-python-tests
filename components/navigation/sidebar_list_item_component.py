from typing import Pattern

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)
        self.identifier = identifier

        self.icon = Icon(page, '{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, '{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page, '{identifier}-drawer-list-item-button', 'Button')

    def assert_visible(self, item_title: str):
        self.icon.assert_visible(identifier=self.identifier)
        self.title.assert_visible(identifier=self.identifier)
        self.title.assert_have_text(text=item_title, identifier=self.identifier)
        self.button.assert_visible(identifier=self.identifier)

    def navigate(self, expected_url: Pattern[str]):
        self.button.click(identifier=self.identifier)
        self.check_current_url(expected_url=expected_url)
