from typing import Literal

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

ChartIdentifier = Literal['students', 'activities', 'courses', 'scores']
ChartType = Literal['bar', 'line', 'pie', 'scatter']


class ChartViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: ChartIdentifier, char_type: ChartType, chart_name: str):
        super().__init__(page=page)

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{char_type}-chart')
        self.chart_name = chart_name

    def assert_visible(self):
        expect(self.chart).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.chart_name)
