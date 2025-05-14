import allure
from playwright.sync_api import Locator, Page, expect

from utils.logger import get_logger


logger = get_logger('BASE_ELEMENT')

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
        step = f'Getting locator with data-testid="{locator}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)  # use `locator` or other search strategy if needed

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

    def assert_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def assert_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that text of {self.type_of} "{self.name}" is "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

    def assert_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that value of {self.type_of} "{self.name}" is "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)
