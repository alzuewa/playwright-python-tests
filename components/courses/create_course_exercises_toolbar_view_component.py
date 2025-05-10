from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create button')

    def assert_visible(self):
        self.title.assert_visible()
        self.title.assert_have_text('Exercises')
        self.create_exercise_button.assert_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
