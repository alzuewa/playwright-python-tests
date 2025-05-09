from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class DashboardToolbarViewComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.title = page.get_by_test_id('dashboard-toolbar-title-text')

    def assert_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Dashboard')
