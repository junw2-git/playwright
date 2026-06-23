from playwright.sync_api import sync_playwright


def run_pick_locator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        # 启动定位器拾取
        page.pick_locator()
        browser.close()


if __name__ == "__main__":
    run_pick_locator()
