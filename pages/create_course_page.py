from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_component import CreateCourseExerciseComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_view_component import ImageUploadViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.navbar = NavbarComponent(page=page)
        self.course_content_form = CreateCourseFormComponent(page=page)
        self.exercise_content_form = CreateCourseExerciseComponent(page=page)
        self.image_upload_view = ImageUploadViewComponent(page=page, identifier='create-course-preview')
        self.toolbar = CreateCourseToolbarViewComponent(page=page, identifier='create-course')
        self.exercises_empty_view = EmptyViewComponent(
            page=page,
            identifier='create-course-exercises',
            title_text='There is no exercises',
            description_text='Click on "Create exercise" button to create new exercise'
        )

        # ===============================
        # Course exercises block locators
        # ===============================
        self.exercises_block_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

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
