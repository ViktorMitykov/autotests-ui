from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent

from playwright.sync_api import Page, expect


class CreateCoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        self.courses_title = page.get_by_test_id("courses-list-toolbar-title-text")

        self.course_widget_title = page.get_by_test_id("course-widget-title-text")
        self.course_widget_preview_image = page.get_by_test_id("course-preview-image")
        self.course_widget_max_score = page.get_by_test_id("course-max-score-info-row-view-text")
        self.course_widget_min_score = page.get_by_test_id("course-min-score-info-row-view-text")
        self.course_widget_estimated_time = page.get_by_test_id("course-estimated-time-info-row-view-text")

        self.courses_list_create_course_button = page.get_by_test_id("courses-list-toolbar-create-course-button")

    def check_visibility_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(title="There is no exercises",
                                                description='Click on "Create exercise" button to create new exercise')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()

    def check_visible_courses_list_create_course_button(self):
        expect(self.courses_list_create_course_button).to_be_visible()

    def check_visisble_course_card(self,
                                    index: int,
                                    title: str,
                                    estimated_time: str,
                                    max_score: str,
                                    min_score: str):
        expect(self.course_widget_title.nth(index)).to_be_visible()
        expect(self.course_widget_title.nth(index)).to_have_text(title)

        expect(self.course_widget_estimated_time.nth(index)).to_be_visible()
        expect(self.course_widget_estimated_time.nth(index)).to_have_text(f"Estimated time: {estimated_time}")

        expect(self.course_widget_max_score.nth(index)).to_be_visible()
        expect(self.course_widget_max_score.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.course_widget_min_score.nth(index)).to_be_visible()
        expect(self.course_widget_min_score.nth(index)).to_have_text(f"Min score: {min_score}")





