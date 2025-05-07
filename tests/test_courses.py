import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from utils.resource_path_getter import get_resource_path

title = 'Playwright'
estimated_time = '2 weeks'
description = 'Playwright'
max_score = 100
min_score = 10


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_be_visible()
    empty_search_results_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_search_results_block).to_be_visible()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.assert_create_course_title_visible()
    create_course_page.assert_create_course_button_disabled()

    create_course_page.assert_preview_empty_view_visible()
    create_course_page.assert_image_upload_view_visible()

    create_course_page.assert_create_course_form_visible(
        title='',
        estimated_time='',
        description='',
        max_score=0,
        min_score=0
    )

    create_course_page.assert_exercises_block_title_visible()
    create_course_page.assert_create_exercise_button_visible()
    create_course_page.assert_exercises_empty_view_visible()

    create_course_page.upload_preview_image(file_path=get_resource_path(local_file_path='testdata/files/image.jpg'))
    create_course_page.assert_image_upload_view_visible(is_image_uploaded=True)

    create_course_page.fill_in_create_course_form(
        title=title,
        estimated_time=estimated_time,
        description=description,
        max_score=max_score,
        min_score=min_score
    )
    create_course_page.click_create_course_button()

    courses_list_page.assert_courses_page_title_visible()
    courses_list_page.assert_create_course_button_visible()
    courses_list_page.assert_course_card_visible(
        index=0,
        title=title,
        max_score=max_score,
        min_score=min_score,
        estimated_time=estimated_time
    )
