import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    time.sleep(1)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    time.sleep(1)
    page.locator("[data-test=\"login-button\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"checkout\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"firstName\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"firstName\"]").fill("marion")
    time.sleep(1)
    page.locator("[data-test=\"lastName\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"lastName\"]").fill("wu")
    time.sleep(1)
    page.locator("[data-test=\"postalCode\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"postalCode\"]").fill("230001")
    time.sleep(1)
    page.locator("[data-test=\"continue\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"finish\"]").click()
    time.sleep(1)
    page.locator("[data-test=\"back-to-products\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
