from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class EmptyViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str, title_text: str, description_text: str):
        super().__init__(page=page)
        self.identifier = identifier
        self.title_text = title_text
        self.description_text = description_text

        self.icon = page.get_by_test_id(f'{self.identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{self.identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{self.identifier}-empty-view-description-text')

    def assert_visible(self):
        expect(self.icon).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.title_text)
        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(self.description_text)
