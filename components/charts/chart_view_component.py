from typing import Literal

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text

ChartIdentifier = Literal['students', 'activities', 'courses', 'scores']
ChartType = Literal['bar', 'line', 'pie', 'scatter']


class ChartViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: ChartIdentifier, char_type: ChartType, chart_name: str):
        super().__init__(page=page)

        self.char_type = char_type
        self.chart_name = chart_name

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{char_type}-chart', 'Chart')

    def assert_visible(self):
        with allure.step(f'Check chart "{self.chart_name}" is visible'):
            self.chart.assert_visible(char_type=self.char_type)
            self.title.assert_visible()
            self.title.assert_have_text(text=self.chart_name)
