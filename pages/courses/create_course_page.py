from playwright.sync_api import Page

from components.courses.create_course_exercise_component import CreateCourseExerciseComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
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
        self.exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page=page)
        self.exercise_content_form = CreateCourseExerciseComponent(page=page)
        self.image_upload_view = ImageUploadViewComponent(page=page, identifier='create-course-preview')
        self.toolbar = CreateCourseToolbarViewComponent(page=page, identifier='create-course')
        self.exercises_empty_view = EmptyViewComponent(
            page=page,
            identifier='create-course-exercises'
        )

    def assert_exercises_empty_view_visible(self):
        self.exercises_empty_view.assert_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
