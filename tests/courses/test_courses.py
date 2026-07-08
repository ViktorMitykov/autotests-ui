import allure
import pytest

from pages.courses.create_course_page import CreateCoursesPage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.tags import AllureTags
from tools.routes import AppRoute
from config import settings


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.REGRESSION, AllureTags.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.story(AllureStory.COURSES)
@allure.feature(AllureFeature.COURSES)
class TestCourses:
    @allure.title("Check displaing of empty courses list")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.check_visability_empty_view()
        courses_list_page.toolbar.check_visible()
        courses_list_page.check_visability_empty_view()

    @allure.title("Create course")
    def test_create_course(self, create_courses_page: CreateCoursesPage, courses_list_page: CoursesListPage):
        create_courses_page.visit(AppRoute.COURSE_CREATE)
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
        create_courses_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_courses_page.create_course_form.fill(title="Playwright",
                                                    estimated_time="2 weeks",
                                                    description="Playwright",
                                                    max_score="100",
                                                    min_score="10")
        create_courses_page.create_course_toolbar.click_create_course_button()

        courses_list_page.toolbar.check_visible()
        courses_list_page.course_card.check_visible(index=0,
                                                    title="Playwright",
                                                    estimated_time="2 weeks",
                                                    max_score="100",
                                                    min_score="10")

    @allure.title("Edit course")
    def test_edit_course(self, create_courses_page: CreateCoursesPage, courses_list_page: CoursesListPage):
        create_courses_page.visit(AppRoute.COURSE_CREATE)
        create_courses_page.create_course_form.fill(title="test course", estimated_time="15",
                                                    description="7.7 Наращивание тестовой базы и рефакторинг",
                                                    max_score="20", min_score="10")

        create_courses_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_courses_page.create_course_form.check_visible(title="test course", estimated_time="15",
                                                             description="7.7 Наращивание тестовой базы и рефакторинг",
                                                             max_score="20", min_score="10")
        create_courses_page.create_course_toolbar.click_create_course_button()

        create_courses_page.check_visisble_course_card(index=0, title="test course", estimated_time="15",
                                                       max_score="20", min_score="10")
        courses_list_page.course_card.menu.click_edit_button()

        create_courses_page.create_course_form.fill(title="test course123", estimated_time="20",
                                                    description="Yo Yo Yo",
                                                    max_score="21", min_score="22")
        create_courses_page.create_course_toolbar.click_create_course_button()

        create_courses_page.check_visisble_course_card(index=0, title="test course123", estimated_time="20",
                                                       max_score="21", min_score="22")
