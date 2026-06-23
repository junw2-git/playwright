import time

from playwright.sync_api import sync_playwright
import time

def test_inventory_page_performance():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        start = time.time()

        page.click("#login-button")
        page.wait_for_selector(".inventory_list")

        end = time.time()
        load_time = end - start
        print(f"商品列表加载时间:{load_time:.2f} s")
        browser.close()