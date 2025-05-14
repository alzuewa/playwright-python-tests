from pathlib import Path

import allure

from elements.base_element import BaseElement
from utils.logger import get_logger


logger = get_logger('FILE_INPUT')

class FileInput(BaseElement):

    def set_input_files(self, file: Path, nth: int = 0, **kwargs):
        step = f'Set file "{file.name}" to {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)
