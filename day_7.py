# https://mp.weixin.qq.com/s/jjfsaP8CWXYCpvSVuZNK9g
import time

from playwright.sync_api import expect, sync_playwright

def test_e2e_purchase():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # stop1 open browser
        page.goto("https://www.saucedemo.com")
        expect(page).to_have_title("Swag Labs")

        # step2 sign in
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        # get shop price
        first_item_price_text = page.locator(
            ".inventory_item_price"
        ).nth(0).text_content()
        first_item_price = float(first_item_price_text.replace("$", ""))

        second_item_price_text = page.locator(
            ".inventory_item_price"
        ).nth(1).text_content()
        second_item_price = float(second_item_price_text.replace("$", ""))

        three_item_price_text = page.locator(
            ".inventory_item_price"
        ).nth(2).text_content()
        three_item_price = float(three_item_price_text.replace("$", ""))

        fourth_item_price_text = page.locator(
            ".inventory_item_price"
        ).nth(3).text_content()
        fourth_item_price = float(fourth_item_price_text.replace("$", ""))

        five_item_price_text = page.locator(
            ".inventory_item_price"
        ).nth(4).text_content()
        five_item_price = float(five_item_price_text.replace("$", ""))

        # step4, add shop box
        time.sleep(1)
        page.click("#add-to-cart-sauce-labs-backpack")
        time.sleep(1)
        page.click("#add-to-cart-sauce-labs-bike-light")
        time.sleep(1)
        page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
        time.sleep(1)
        page.click("#add-to-cart-sauce-labs-fleece-jacket")
        time.sleep(1)
        page.click("#add-to-cart-sauce-labs-onesie")
        time.sleep(1)
        # page.click("add-to-cart-test.allthethings()-t-shirt-(red)")
        # time.sleep(1)
        expect(page.locator(".shopping_cart_badge")).to_have_text("5")


        # step5 goto shop box
        page.click(".shopping_cart_link")
        expect(page).to_have_url("https://www.saucedemo.com/cart.html")

        # step6 click checkout button
        page.click("#checkout")
        expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

        # step 7 fill text
        page.fill("#first-name", "Marion")
        page.fill("#last-name", "wu")
        page.fill("#postal-code", "230001")
        page.click("#continue")

        # step 8 verify total price
        expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
        item_total_text = page.locator(".summary_subtotal_label").text_content()
        import re
        summary_subtotal_label = float(re.search(r"[\d.]+", item_total_text).group())
        summary_total_label = first_item_price + second_item_price + three_item_price + fourth_item_price + five_item_price + 9.12
        assert abs(summary_total_label - summary_subtotal_label) <= 9.13, \
            f"总价不匹配：期望 {summary_total_label}, 实际 {summary_subtotal_label}"

        browser.close()
        print("✅ 全链路测试通过！")

if __name__ == "__main__":
    test_e2e_purchase()
