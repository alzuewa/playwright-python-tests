from pathlib import Path

from elements.base_element import BaseElement


class FileInput(BaseElement):

    def set_input_files(self, file: str | Path, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(file)
