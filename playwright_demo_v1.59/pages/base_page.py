from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # 打开网址
    def goto(self, url: str):
        self.page.goto(url)

    # 元素点击
    def click(self, locator: str):
        self.page.locator(locator).click()

    # 输入文本
    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    # 等待元素可见
    def wait_for_visible(self, locator: str, timeout: int = 10000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    #
    def wait_url_contains(self, keyword, timeout=5000):
        self.page.wait_for_url(f"**{keyword}**", timeout=timeout)

    # 断言文本
    def assert_text(self, locator: str, expect_text: str):
        expect(self.page.locator(locator)).to_have_text(expect_text)

    # 获取URL
    def get_url(self) -> str:
        return self.page.url