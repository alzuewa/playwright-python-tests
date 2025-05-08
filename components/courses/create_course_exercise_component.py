from playwright.sync_api import expect

from components.base_component import BaseComponent


class CreateCourseExerciseComponent(BaseComponent):

    def click_delete_button(self, index: int):
        delete_button = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        delete_button.click()

    def fill_in_exercise_form(self, index: int, title: str, description: str):
        title_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        description_input = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{index}-input'
        ).locator('input')

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)

    def assert_form_visible(self, index: int, title: str, description: str):
        heading = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        title_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        description_input = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{index}-input'
        ).locator('input')

        expect(heading).to_be_visible()
        expect(heading).to_have_text(f'#{index + 1} Exercise')

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)
