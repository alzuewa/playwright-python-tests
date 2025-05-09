import pytest

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
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_list_page.navbar.assert_visible(username='username')
    courses_list_page.sidebar.assert_visible()

    courses_list_page.toolbar.assert_visible()
    courses_list_page.assert_empty_view_visible()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.toolbar.assert_visible(is_create_course_disabled=True)
    create_course_page.image_upload_view.assert_visible(is_image_uploaded=False)
    create_course_page.course_content_form.assert_visible(
        title='',
        estimated_time='',
        description='',
        max_score=0,
        min_score=0
    )
    create_course_page.assert_exercises_block_title_visible()
    create_course_page.assert_create_exercise_button_visible()
    create_course_page.assert_exercises_empty_view_visible()
    create_course_page.image_upload_view.upload_preview_image(
        file_path=get_resource_path(local_file_path='testdata/files/image.jpg')
    )
    create_course_page.image_upload_view.assert_visible(is_image_uploaded=True)
    create_course_page.course_content_form.fill_form(
        title=title,
        estimated_time=estimated_time,
        description=description,
        max_score=max_score,
        min_score=min_score
    )
    create_course_page.toolbar.click_create_course_button()
    courses_list_page.toolbar.assert_visible()
    courses_list_page.course_view.assert_visible(
        index=0,
        title=title,
        max_score=max_score,
        min_score=min_score,
        estimated_time=estimated_time
    )
