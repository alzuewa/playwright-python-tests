import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)

        self.title = Text(page, f'{identifier}-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, f'{identifier}-toolbar-create-course-button', 'Create button')

    def assert_visible(self, is_create_course_disabled=True):
        self.title.assert_visible()
        self.title.assert_have_text(text='Create course')
        self.create_course_button.assert_visible()
        if is_create_course_disabled:
            self.create_course_button.assert_disabled()
        else:
            self.create_course_button.assert_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(expected_url=re.compile('.*/#/courses'))
