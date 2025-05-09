from typing import Literal

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text

ChartIdentifier = Literal['students', 'activities', 'courses', 'scores']
ChartType = Literal['bar', 'line', 'pie', 'scatter']


class ChartViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: ChartIdentifier, char_type: ChartType, chart_name: str):
        super().__init__(page=page)

        self.identifier = identifier
        self.char_type = char_type
        self.chart_name = chart_name

        self.title = Text(page, '{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, '{identifier}-{char_type}-chart', 'Chart')

    def assert_visible(self):
        self.chart.assert_visible(identifier=self.identifier, char_type=self.char_type)
        self.title.assert_visible(identifier=self.identifier)
        self.title.assert_have_text(text=self.chart_name, identifier=self.identifier)
