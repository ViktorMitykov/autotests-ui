import re

import allure

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent

from playwright.sync_api import Page, expect


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard = SidebarListItemComponent(page, "dashboard")
        self.courses = SidebarListItemComponent(page, "courses")
        self.logout = SidebarListItemComponent(page, "logout")

    @allure.step("Check visible sidebar")
    def check_visible(self):
        self.dashboard.check_visible("Dashboard")
        self.courses.check_visible("Courses")
        self.logout.check_visible("Logout")

    @allure.step("Click dashboard on sidebar")
    def click_dashboard(self):
        self.dashboard.navigate(re.compile(r".*/#/dashboard"))

    @allure.step("Click courses on sidebar")
    def click_courses(self):
        self.courses.navigate(re.compile(r".*/#/courses"))

    @allure.step("Click logout on sidebar")
    def click_logout(self):
        self.logout.navigate(re.compile(r".*/#/auth/login"))