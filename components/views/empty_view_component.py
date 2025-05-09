from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class EmptyViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)
        self.identifier = identifier

        self.icon = page.get_by_test_id(f'{self.identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{self.identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{self.identifier}-empty-view-description-text')

    def assert_visible(self, title: str, description: str):
        expect(self.icon).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)
