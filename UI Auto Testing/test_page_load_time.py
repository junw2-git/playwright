import time
from playwright.sync_api import sync_playwright

def test_page_load_time():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        start = time.time()
        print("\n")
        print("start time:", start)
        page.goto("https://www.saucedemo.com")
        end = time.time()
        print("end time:", end)

        load_time = end - start
        print(f"页面加载时间: {load_time:.2f} 秒")
        browser.close()