import re
from dataclasses import dataclass

import allure
import pytest
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.resource_path_getter import get_resource_path


@dataclass
class CourseData:
    title: str
    estimated_time: str
    description: str
    max_score: int
    min_score: int


empty_data = CourseData(title='', estimated_time='', description='', min_score=0, max_score=0)
first_data = CourseData(
    title='Playwright', estimated_time='2 weeks', description='Playwright', min_score=100, max_score=10
)


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:

    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_page.navbar.assert_visible(username='username')
        courses_list_page.sidebar.assert_visible()

        courses_list_page.toolbar.assert_visible()
        courses_list_page.assert_empty_view_visible()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.toolbar.assert_visible(is_create_course_disabled=True)
        create_course_page.image_upload_view.assert_visible(is_image_uploaded=False)
        create_course_page.course_content_form.assert_visible(
            title_text=empty_data.title,
            estimated_time=empty_data.estimated_time,
            description=empty_data.description,
            max_score=empty_data.max_score,
            min_score=empty_data.min_score
        )
        create_course_page.exercise_toolbar.assert_visible()
        create_course_page.assert_exercises_empty_view_visible()
        create_course_page.image_upload_view.upload_preview_image(
            file_path=get_resource_path(local_file_path='testdata/files/image.jpg')
        )
        create_course_page.image_upload_view.assert_visible(is_image_uploaded=True)
        create_course_page.course_content_form.fill(
            title_text=first_data.title,
            estimated_time=first_data.estimated_time,
            description=first_data.description,
            max_score=first_data.max_score,
            min_score=first_data.min_score
        )
        create_course_page.toolbar.click_create_course_button()
        courses_list_page.toolbar.assert_visible()
        courses_list_page.course_view.assert_visible(
            index=0,
            title_text=first_data.title,
            estimated_time=first_data.estimated_time,
            max_score=first_data.max_score,
            min_score=first_data.min_score
        )

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(
            self,
            courses_list_page: CoursesListPage,
            create_course_page_authorized: CreateCoursePage
    ):
        edited_data = CourseData(
            title='Awesome Playwright', estimated_time='1 month', description='This is fun', max_score=200,
            min_score=100
        )
        create_course_page_authorized.open(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page_authorized.course_content_form.fill(
            title_text=first_data.title,
            estimated_time=first_data.estimated_time,
            description=first_data.description,
            max_score=first_data.max_score,
            min_score=first_data.min_score
        )
        create_course_page_authorized.image_upload_view.upload_preview_image(
            file_path=get_resource_path(local_file_path='testdata/files/image.jpg')
        )
        create_course_page_authorized.toolbar.click_create_course_button()

        courses_list_page.check_current_url(expected_url=re.compile('.*/#/courses'))
        courses_list_page.course_view.assert_visible(
            index=0,
            title_text=first_data.title,
            estimated_time=first_data.estimated_time,
            max_score=first_data.max_score,
            min_score=first_data.min_score
        )
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page_authorized.course_content_form.fill(
            title_text=edited_data.title,
            estimated_time=edited_data.estimated_time,
            description=edited_data.description,
            min_score=edited_data.min_score,
            max_score=edited_data.max_score
        )
        create_course_page_authorized.toolbar.click_create_course_button()
        courses_list_page.course_view.assert_visible(
            index=0,
            title_text=edited_data.title,
            estimated_time=edited_data.estimated_time,
            max_score=edited_data.max_score,
            min_score=edited_data.min_score
        )
