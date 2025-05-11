import allure
from playwright.sync_api import Locator, Page, expect


class BaseElement:

    def __init__(self, page: Page, locator_pattern: str, name: str):
        self.page = page
        self.locator_pattern = locator_pattern
        self.name = name

    @property
    def type_of(self) -> str:
        return self.__class__.__name__

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator_pattern.format(**kwargs)
        with allure.step(f'Getting locator with data-testid="{locator}" at index "{nth}"'):
            return self.page.get_by_test_id(locator).nth(nth)  # use `locator` or other search strategy if needed

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Clicking {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def assert_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} is visible'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def assert_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} text is "{text}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)

    def assert_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that value of {self.type_of} is "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)