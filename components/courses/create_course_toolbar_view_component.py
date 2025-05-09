import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)
        self.identifier = identifier

        self.title = page.get_by_test_id(f'{self.identifier}-toolbar-title-text')
        self.create_course_button = page.get_by_test_id(f'{self.identifier}-toolbar-create-course-button')

    def assert_visible(self, is_create_course_disabled=True):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Create course')
        expect(self.create_course_button).to_be_visible()
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()
        else:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(expected_url=re.compile('.*/#/courses'))
