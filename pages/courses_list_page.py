from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CoursesListPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.courses_page_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')
        self.course_context_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')

    def assert_courses_page_title_visible(self):
        expect(self.courses_page_title).to_be_visible()
        expect(self.courses_page_title).to_have_text('Courses')

    def assert_empty_view_visible(self):
        expect(self.empty_view_icon).to_be_visible()
        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')
        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')

    def assert_create_course_button_visible(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def assert_course_card_visible(
            self,
            index: int,
            title: str,
            max_score: int,
            min_score: int,
            estimated_time: str
    ):
        expect(self.course_image.nth(index=index)).to_be_visible()
        expect(self.course_title.nth(index=index)).to_be_visible()
        expect(self.course_title.nth(index=index)).to_have_text(title)
        expect(self.course_max_score_text.nth(index=index)).to_be_visible()
        expect(self.course_max_score_text.nth(index=index)).to_have_text(f'Max score: {max_score}')
        expect(self.course_min_score_text.nth(index=index)).to_be_visible()
        expect(self.course_min_score_text.nth(index=index)).to_have_text(f'Min score: {min_score}')
        expect(self.course_estimated_time_text.nth(index=index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index=index)).to_have_text(f'Estimated time: {estimated_time}')

    def click_edit_course(self, index: int):
        self.course_context_menu_button.nth(index=index).click()
        expect(self.course_edit_menu_button).to_be_visible()
        self.course_edit_menu_button.click()

    def click_delete_course(self, index: int):
        self.course_context_menu_button.nth(index=index).click()
        expect(self.course_delete_menu_button).to_be_visible()
        self.course_delete_menu_button.click()
