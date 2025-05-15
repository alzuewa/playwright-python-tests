import allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement
from utils.logger import get_logger


logger = get_logger('INPUT')

class Input(BaseElement):

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Set to {self.type_of} "{self.name}" value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def assert_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that value of {self.type_of} "{self.name}" is "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)
