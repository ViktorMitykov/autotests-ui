import allure
import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.tags import AllureTags
from tools.routes import AppRoute
from allure_commons.types import Severity




class TestRegistration:
    @pytest.mark.xdist_group("authorization-group")
    @pytest.mark.regression
    @pytest.mark.registration
    @allure.title("Registration with correct email, username and password")
    @allure.tag(AllureTags.REGISTRATION, AllureTags.REGRESSION)
    @allure.epic(AllureEpic.LMS)
    @allure.feature(AllureFeature.AUTHENTICATION)
    @allure.story(AllureStory.REGISTRATION)
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill("test@mail.ru", "username12313", "sadsadada")
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()