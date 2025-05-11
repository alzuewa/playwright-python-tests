import allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement

class Textarea(BaseElement):

    def get_locator(self, nth: int = 0,**kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Set to {self.type_of} "{self.name}" value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)
