import pytest
from playwright.sync_api import sync_playwright
from utils.api_client import ApiClient

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def api_client():
    return ApiClient()

