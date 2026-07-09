import allure
import pytest

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.tags import AllureTags
from tools.routes import AppRoute
from config import settings


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTags.REGRESSION, AllureTags.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.story(AllureStory.DASHBOARD)
@allure.feature(AllureFeature.DASHBOARD)
class TestDashboard:
    @allure.title("Check displaying of dashboard page")
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()



print(123567)