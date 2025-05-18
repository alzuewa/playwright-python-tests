import allure
from playwright.sync_api import Locator, Page, expect
from ui_coverage_tool import ActionType, SelectorType

from elements.ui_coverage import tracker
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

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f'//*[@data-testid="{self.locator_pattern.format(**kwargs)}"][{nth + 1}]'

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def assert_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)

    def assert_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that text of {self.type_of} "{self.name}" is "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)
