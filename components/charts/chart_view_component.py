import allure
from playwright.sync_api import expect

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', "title")
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', "chart")

    @allure.step('Check visible chart view "{title}"')
    def visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(text=title)

        self.chart.check_visible()