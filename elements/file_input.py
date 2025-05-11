from pathlib import Path

import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):

    def set_input_files(self, file: Path, nth: int = 0, **kwargs):
        with allure.step(f'Set file "{file.name}" to {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
