import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
from utils.routes import AppRoute


class CoursesListToolbarViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)
        self.identifier = identifier

        self.title = Text(page, f'{identifier}-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, f'{identifier}-toolbar-create-course-button', 'Create course')

    @allure.step('Check courses list toolbar is visible')
    def assert_visible(self):
        self.title.assert_visible()
        self.title.assert_have_text(text='Courses')
        self.create_course_button.assert_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(expected_url=re.compile(r'.*/#/courses/create'))
