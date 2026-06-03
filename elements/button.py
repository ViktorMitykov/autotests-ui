from playwright.sync_api import expect

from elements.base_element import BaseElement

class Button(BaseElement):
    def check_enabled(self, **kwargs):
        locator = self.get_locator(**kwargs)

    def check_disabled(self, **kwagrs):
        locator = self.get_locator(**kwagrs)
        expect(locator).to_be_disabled()