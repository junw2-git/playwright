from playwright.sync_api import Page, expect, sync_playwright

def test_login_error_message(page: Page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")

    # 这行会挂——#this-locator-does-not-exist 不存在
    error = page.text_content("#this-locator-does-not-exist")
    assert error is not None
