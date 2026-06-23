import time

from playwright.sync_api import sync_playwright


def run_screencast():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # 开启录屏，视频保存到 reports 目录
        context = browser.new_context(record_video_dir="reports/videos/")
        # context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        time.sleep(3)

        context.close()
        browser.close()


if __name__ == "__main__":
    run_screencast()
