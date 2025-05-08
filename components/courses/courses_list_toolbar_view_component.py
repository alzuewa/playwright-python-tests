import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CoursesListToolbarViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str, title_text: str):
        super().__init__(page=page)
        self.identifier = identifier
        self.title_text = title_text

        self.title = page.get_by_test_id(f'{self.identifier}-toolbar-title-text')
        self.create_course_button = page.get_by_test_id(f'{self.identifier}-toolbar-create-course-button')

    def assert_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.title_text)
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(expected_url=re.compile('.*/#/courses/create'))

    def click_save_course_button(self):
        self.create_course_button.click()
        self.check_current_url(expected_url=re.compile('.*/#/courses'))

    def assert_create_course_button_disabled(self):
        expect(self.create_course_button).to_be_disabled()
