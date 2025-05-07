from pathlib import Path

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateCoursePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        # ====================================
        # Course creation upper block locators
        # ====================================
        self.create_course_page_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        # ===========================
        # Course image block locators
        # ===========================
        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        self.image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.image_upload_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.image_upload_description = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-description-text')
        self.image_upload_button = page.get_by_test_id('create-course-preview-image-upload-widget-input')
        self.image_remove_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

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
        self.exercises_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_view_description = page.get_by_test_id(
            'create-course-exercises-empty-view-description-text')

    # ===================================
    # Course creation upper block methods
    # ===================================
    def assert_create_course_title_visible(self):
        expect(self.create_course_page_title).to_be_visible()
        expect(self.create_course_page_title).to_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()

    def assert_create_course_button_visible(self):
        expect(self.create_course_button).to_be_visible()

    def assert_create_course_button_disabled(self):
        expect(self.create_course_button).to_be_disabled()

    # ==========================
    # Course image block methods
    # ==========================
    def assert_preview_empty_view_visible(self):
        expect(self.preview_empty_view_icon).to_be_visible()
        expect(self.preview_empty_view_title).to_be_visible()
        expect(self.preview_empty_view_title).to_have_text('No image selected')
        expect(self.preview_empty_view_description).to_be_visible()
        expect(self.preview_empty_view_description).to_have_text('Preview of selected image will be displayed here')

    def assert_image_upload_view_visible(self, is_image_uploaded: bool = False):
        expect(self.image_upload_icon).to_be_visible()
        expect(self.image_upload_title).to_be_visible()
        expect(self.image_upload_title).to_have_text('Tap on "Upload image" button to select file')
        expect(self.image_upload_description).to_be_visible()
        expect(self.image_upload_description).to_have_text('Recommended file size 540X300')
        expect(self.image_upload_button).to_be_visible()
        if is_image_uploaded:
            expect(self.image_remove_button).to_be_visible()

    def click_remove_image_button(self):
        self.image_remove_button.click()

    def upload_preview_image(self, file_path: str | Path):
        self.image_upload_button.set_input_files(file_path)

    def assert_preview_image_visible(self):
        expect(self.preview_image).to_be_visible()

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
        expect(self.exercises_empty_view_icon).to_be_visible()
        expect(self.exercises_empty_view_title).to_be_visible()
        expect(self.exercises_empty_view_title).to_have_text('There is no exercises')
        expect(self.exercises_empty_view_description).to_be_visible()
        expect(self.exercises_empty_view_description).to_have_text(
            'Click on "Create exercise" button to create new exercise')

    # =============================
    # Edit course exercises methods
    # =============================
    def click_delete_exercise_button(self, index: int):
        delete_exercise_button = self.page.get_by_test_id(
            f'create-course-exercise-{index}-box-toolbar-delete-exercise-button'
        )
        delete_exercise_button.click()

    def fill_in_exercise_form(self, index: int, title: str, description: str):
        exercise_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        exercise_description = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{index}-input'
        ).locator('input')

        exercise_title.fill(title)
        expect(exercise_title).to_have_value(title)

        exercise_description.fill(description)
        expect(exercise_description).to_have_value(description)

    def assert_exercise_form_visible(self, index: int, title: str, description: str):
        exercise_heading = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        exercise_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        exercise_description = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{index}-input'
        ).locator('input')

        expect(exercise_heading).to_be_visible()
        expect(exercise_heading).to_have_text(f'#{index + 1} Exercise')

        expect(exercise_title).to_be_visible()
        expect(exercise_title).to_have_value(title)

        expect(exercise_description).to_be_visible()
        expect(exercise_description).to_have_value(description)
