from playwright.sync_api import Page, expect

from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.create_course_exercise_component import CreateCourseExerciseComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_view_component import ImageUploadViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.navbar = NavbarComponent(page=page)
        self.create_course_form = CreateCourseExerciseComponent(page=page)
        self.toolbar = CoursesListToolbarViewComponent(page=page, identifier='create-course',
                                                       title_text='Create course')
        self.image_upload_view = ImageUploadViewComponent(page=page, identifier='create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(
            page=page,
            identifier='create-course-exercises',
            title_text='There is no exercises',
            description_text='Click on "Create exercise" button to create new exercise'
        )

        # =========================
        # Course text form locators
        # =========================
        self.course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.course_estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator(
            'input')
        self.course_description_input = page.get_by_test_id('create-course-form-description-input').locator(
            'textarea').first
        self.max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        # ===============================
        # Course exercises block locators
        # ===============================
        self.exercises_block_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    # ========================
    # Course text form methods
    # ========================
    def fill_in_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: int,
            min_score: int
    ):
        self.course_title_input.fill(title)
        expect(self.course_title_input).to_have_value(title)

        self.course_estimated_time_input.fill(estimated_time)
        expect(self.course_estimated_time_input).to_have_value(estimated_time)

        self.course_description_input.fill(description)
        expect(self.course_description_input).to_have_value(description)

        self.max_score_input.fill(str(max_score))
        expect(self.max_score_input).to_have_value(str(max_score))

        self.min_score_input.fill(str(min_score))
        expect(self.min_score_input).to_have_value(str(min_score))

    def assert_create_course_form_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: int,
            min_score: int
    ):
        expect(self.course_title_input).to_be_visible()
        expect(self.course_title_input).to_have_value(title)

        expect(self.course_estimated_time_input).to_be_visible()
        expect(self.course_estimated_time_input).to_have_value(estimated_time)

        expect(self.course_description_input).to_be_visible()
        expect(self.course_description_input).to_have_value(description)

        expect(self.max_score_input).to_be_visible()
        expect(self.max_score_input).to_have_value(str(max_score))

        expect(self.min_score_input).to_be_visible()
        expect(self.min_score_input).to_have_value(str(min_score))

    # ==============================
    # Course exercises block methods
    # ==============================
    def assert_exercises_block_title_visible(self):
        expect(self.exercises_block_title).to_be_visible()
        expect(self.exercises_block_title).to_have_text('Exercises')

    def assert_create_exercise_button_visible(self):
        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()

    def assert_exercises_empty_view_visible(self):
        self.exercises_empty_view.assert_visible()
