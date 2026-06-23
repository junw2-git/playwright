import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# 全局启动/关闭浏览器
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        yield browser
        browser.close()

# 新建页面
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    context.close()

# 登录页对象
@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)

# 商品页对象
@pytest.fixture(scope="function")
def inventory_page(page):
    return InventoryPage(page)