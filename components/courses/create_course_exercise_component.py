import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input


class CreateCourseExerciseComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.delete_exercise_button = Button(
            page, 'create-course-exercise-{index}-box-toolbar-delete-exercise-button', 'Delete exercise'
        )
        self.title = Input(
            page, 'create-course-exercise-form-title-{index}-input', 'Title'
        )
        self.subtitle_input = Input(
            page, 'create-course-exercise-{index}-box-toolbar-subtitle-text', 'Subtitle'
        )
        self.description_input = Input(
            page, 'create-course-exercise-form-description-{index}-input', 'Exercise description'
        )

    def click_delete_button(self, index: int):
        self.delete_exercise_button.click(index=index)

    @allure.step('Fill in course exercise form at index "{index}"')
    def fill(self, index: int, title: str, description: str):
        self.subtitle_input.fill(value=title, index=index)
        self.subtitle_input.assert_have_value(value=title, index=index)

        self.description_input.fill(value=description, index=index)
        self.description_input.assert_have_value(value=description, index=index)

    @allure.step('Check course exercise form at index "{index}" is visible')
    def assert_form_visible(self, index: int, title: str, description: str):
        self.title.assert_visible(index=index)
        self.title.assert_have_text(text=f'#{index + 1} Exercise', index=index)

        self.subtitle_input.assert_visible()
        self.subtitle_input.assert_have_value(value=title, index=index)

        self.description_input.assert_visible(index=index)
        self.description_input.assert_have_value(value=description, index=index)
