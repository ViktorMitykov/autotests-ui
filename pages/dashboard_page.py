from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent

from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

        self.students_title = page.get_by_test_id("students-widget-title-text")
        self.students_widget = page.get_by_test_id("students-bar-chart")

        self.activities_title = page.get_by_test_id("activities-widget-title-text")
        self.activities_widget = page.get_by_test_id("activities-line-chart")

        self.courses_title = page.get_by_test_id("courses-widget-title-text")
        self.courses_widget = page.get_by_test_id("courses-pie-chart")

        self.scores_title = page.get_by_test_id("scores-widget-title-text")
        self.scores_widget = page.get_by_test_id("scores-scatter-chart")

    def check_visible_students_chart(self):
        expect(self.students_title).to_be_visible()
        expect(self.students_widget).to_be_visible()
        expect(self.students_title).to_have_text("Students")

    def check_visible_activities_chart(self):
        expect(self.activities_title).to_be_visible()
        expect(self.activities_widget).to_be_visible()
        expect(self.activities_title).to_have_text("Activities")

    def check_visible_courses_chart(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_widget).to_be_visible()
        expect(self.courses_title).to_have_text("Courses")

    def check_visible_scores_chart(self):
        expect(self.scores_title).to_be_visible()
        expect(self.scores_widget).to_be_visible()
        expect(self.scores_title).to_have_text("Scores")
