# conftest.py （必须放在项目根目录）
import pytest
from playwright.sync_api import sync_playwright


# 注意：def 前面不能有缩进！！！
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        yield page  # 必须返回 page

        # 测试结束后关闭
        browser.close()
