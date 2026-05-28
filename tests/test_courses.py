import pytest

from pages.create_course_page import CreateCoursesPage
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username")
    courses_list_page.check_visability_empty_view()
    courses_list_page.toolbar.check_visible_create_course_button()
    courses_list_page.check_visability_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_courses_page: CreateCoursesPage, courses_list_page: CoursesListPage):
    create_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_courses_page.create_course_toolbar.check_visible()
    create_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_courses_page.create_course_form.check_visible(title="",
                                                         description="",
                                                         estimated_time="",
                                                         max_score="0",
                                                         min_score="0")
    create_courses_page.check_visibility_exercises_empty_view()
    create_courses_page.create_exercise_toolbar.check_visible()
    create_courses_page.check_visibility_exercises_empty_view()
    create_courses_page.image_upload_widget.upload_preview_image("testdata/files/image.jpg")
    create_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_courses_page.create_course_form.fill(title="Playwright",
                                                estimated_time="2 weeks",
                                                description="Playwright",
                                                max_score="100",
                                                min_score="10")
    create_courses_page.create_course_toolbar.click_create_course_button()

    courses_list_page.toolbar.check_visibile_courses_title()
    courses_list_page.toolbar.check_visible_create_course_button()
    courses_list_page.course_card.check_visible(index=0,
                                                title="Playwright",
                                                estimated_time="2 weeks",
                                                max_score="100",
                                                min_score="10")
