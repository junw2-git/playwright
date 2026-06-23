from playwright.sync_api import sync_playwright
import time


def test_api_response_time():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        print("\n")

        def log_response(response):
            if "baidu" in response.url:
                print("接口:", response.url)
                print("状态:", response.status)

        page.on("response", log_response)
        page.goto("https://www.baidu.com")
        browser.close()
