import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="地图").click()
    page1 = page1_info.value
    page1.locator(".searchbox-content-button").click()
    page1.get_by_role("textbox", name="输入起点或在图区上选点").click()
    page1.get_by_role("textbox", name="输入起点或在图区上选点").fill("保利海上五月花- B区")
    page1.get_by_role("textbox", name="输入终点").click()
    page1.get_by_role("textbox", name="输入终点").fill("合肥市政府")
    page1.get_by_text("合肥市人民政府 合肥市蜀山区").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
