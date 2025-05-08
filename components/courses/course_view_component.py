from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent


class CourseViewComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.menu = CourseViewMenuComponent(page=page)

        self.title = page.get_by_test_id('course-widget-title-text')
        self.image = page.get_by_test_id('course-preview-image')
        self.max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

    def assert_visible(self, index: int, title: str, max_score: int, min_score: int, estimated_time: str):
        expect(self.image.nth(index=index)).to_be_visible()
        expect(self.title.nth(index=index)).to_be_visible()
        expect(self.title.nth(index=index)).to_have_text(title)
        expect(self.max_score_text.nth(index=index)).to_be_visible()
        expect(self.max_score_text.nth(index=index)).to_have_text(f'Max score: {max_score}')
        expect(self.min_score_text.nth(index=index)).to_be_visible()
        expect(self.min_score_text.nth(index=index)).to_have_text(f'Min score: {min_score}')
        expect(self.estimated_time_text.nth(index=index)).to_be_visible()
        expect(self.estimated_time_text.nth(index=index)).to_have_text(f'Estimated time: {estimated_time}')
