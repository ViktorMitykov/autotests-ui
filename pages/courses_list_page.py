from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.courses_view_component import CourseViewComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage

from playwright.sync_api import Page


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.empty_view = EmptyViewComponent(page, "courses-list")
        self.course_card = CourseViewComponent(page)
        self.toolbar = CoursesListToolbarViewComponent(page)

    def check_visability_empty_view(self):
        self.empty_view.check_visible(title="There is no results",
                                      description="Results from the load test pipeline will be displayed here")






