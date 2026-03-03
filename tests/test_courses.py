from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("test@mail.ru")

        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username1")

        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password1")

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")

        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        title = page.get_by_test_id("courses-list-toolbar-title-text")
        title.text_content()

        courses_div = page.get_by_test_id("courses-list-empty-view-title-text")
        empty_courses_img = page.get_by_test_id("courses-list-empty-view-icon")
        courses_list = page.get_by_test_id("courses-list-empty-view-description-text")

        expect(title).to_have_text("Courses")
        expect(courses_div).to_be_visible()
        expect(courses_div).to_have_text("There is no results")
        expect(empty_courses_img).to_be_visible()
        expect(courses_list).to_have_text("Results from the load test pipeline will be displayed here")

