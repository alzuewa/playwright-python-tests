from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, wait_until='load')

    def reload(self):
        self.page.reload(wait_until='load')
