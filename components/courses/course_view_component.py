import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.menu = CourseViewMenuComponent(page=page)

        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.image = Image(page, 'course-preview-image', 'Preview')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated time')

    @allure.step('Check course view at index "{index}" is visible')
    def assert_visible(self, index: int, title_text: str, max_score: int, min_score: int, estimated_time: str):
        self.image.assert_visible(nth=index)
        self.title.assert_visible(nth=index)
        self.title.assert_have_text(text=title_text, nth=index)
        self.max_score_text.assert_visible(nth=index)
        self.max_score_text.assert_have_text(text=f'Max score: {max_score}', nth=index)
        self.min_score_text.assert_visible(nth=index)
        self.min_score_text.assert_have_text(text=f'Min score: {min_score}', nth=index)
        self.estimated_time_text.assert_visible(nth=index)
        self.estimated_time_text.assert_have_text(text=f'Estimated time: {estimated_time}', nth=index)
