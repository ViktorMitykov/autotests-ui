from playwright.sync_api import Page
import pytest

from fixtures.browser import chromium_page_with_state
from pages.create_course_page import CreateCoursesPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.courses_list_page import CoursesListPage


@pytest.fixture()
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(chromium_page)


@pytest.fixture()
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(chromium_page)


@pytest.fixture()
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(chromium_page)


@pytest.fixture()
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(chromium_page_with_state)


@pytest.fixture()
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(chromium_page_with_state)

@pytest.fixture()
def create_courses_page(chromium_page_with_state: Page) -> CreateCoursesPage:
    return CreateCoursesPage(chromium_page_with_state)
