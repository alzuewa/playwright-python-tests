from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)
        self.identifier = identifier

        self.icon = Icon(page, '{identifier}-empty-view-icon', 'Icon')
        self.title = Text(page, '{identifier}-empty-view-title-text', 'Title')
        self.description = Text(page, '{identifier}-empty-view-description-text', 'Description')

    def assert_visible(self, title: str, description: str):
        self.icon.assert_visible(identifier=self.identifier)
        self.title.assert_visible(identifier=self.identifier)
        self.title.assert_have_text(text=title, identifier=self.identifier)
        self.description.assert_visible(identifier=self.identifier)
        self.description.assert_have_text(text=description, identifier=self.identifier)
