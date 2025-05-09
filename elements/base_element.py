from playwright.sync_api import Locator, Page, expect


class BaseElement:

    def __init__(self, page: Page, locator_pattern: str, name: str):
        self.page = page
        self.locator_pattern = locator_pattern
        self.name = name

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator_pattern.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)  # use `locator` or other search strategy if needed

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def assert_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def assert_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)

    def assert_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(value)