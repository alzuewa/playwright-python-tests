from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Title')
        self.estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Estimated time')
        self.description_input = Textarea(page, 'create-course-form-description-input', 'Description')
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score')

    def fill(self, title_text: str, estimated_time: str, description: str, max_score: int, min_score: int):
        self.title_input.fill(value=title_text)
        self.title_input.assert_have_value(value=title_text)

        self.estimated_time_input.fill(value=estimated_time)
        self.estimated_time_input.assert_have_value(value=estimated_time)

        self.description_input.fill(value=description)
        self.description_input.assert_have_value(description)

        self.max_score_input.fill(value=str(max_score))
        self.max_score_input.assert_have_value(value=str(max_score))

        self.min_score_input.fill(value=str(min_score))
        self.min_score_input.assert_have_value(value=str(min_score))

    def assert_visible(self, title_text: str, estimated_time: str, description: str, max_score: int, min_score: int):
        self.title_input.assert_visible()
        self.title_input.assert_have_value(value=title_text)

        self.estimated_time_input.assert_visible()
        self.estimated_time_input.assert_have_value(value=estimated_time)

        self.description_input.assert_visible()
        self.description_input.assert_have_value(value=description)

        self.max_score_input.assert_visible()
        self.max_score_input.assert_have_value(value=str(max_score))

        self.min_score_input.assert_visible()
        self.min_score_input.assert_have_value(value=str(min_score))
