from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    def __init__(self, page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def visible(self, title: str):
        expect(title).to_be_visible()
        expect(title).to_have_text(title)

        expect(self.chart).to_be_visible()