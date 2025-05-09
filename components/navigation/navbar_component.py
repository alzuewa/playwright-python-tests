from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome text')

    def assert_visible(self, username: str):
        self.app_title.assert_visible()
        self.app_title.assert_have_text(text='UI Course')

        self.welcome_title.assert_visible()
        self.welcome_title.assert_have_text(text=f'Welcome, {username}!')
