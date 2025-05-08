from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str, item_name: str):
        super().__init__(page=page)
        self.identifier = identifier
        self.item_name = item_name

        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

    def assert_visible(self):
        expect(self.icon).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.item_name)
        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url=expected_url)
