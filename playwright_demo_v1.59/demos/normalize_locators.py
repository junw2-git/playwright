from playwright.sync_api import sync_playwright


def run_normalize():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        loc = page.locator("#login-button")
        # 标准化定位器输出
        print(loc.normalize())
        browser.close()


if __name__ == "__main__":
    run_normalize()
