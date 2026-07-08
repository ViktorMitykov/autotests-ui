import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.view_menu_button = Button(page, "course-view-menu-button", "menu")
        self.edit_menu_button = Button(page, "course-view-edit-menu-item-text", "edit")
        self.delete_menu_button = Button(page, "course-view-edit-menu-item-text", "delete")

    @allure.step('Open course menu at index "{index}" and click edit')
    def click_edit_button(self, index: int = 0):
        self.view_menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    @allure.step('Open course menu at index "{index}" and click delete')
    def click_delete_button(self, index: int = 0):
        self.view_menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)