import time


def test_login_success(login_page, inventory_page):
    # 打开被测站点
    login_page.goto("https://www.saucedemo.com")
    # 执行登录
    login_page.login("standard_user", "secret_sauce")
    # 关键：等待跳转至商品页面URL，确认页面加载完成
    inventory_page.wait_url_contains("/inventory.html")
    # 断言跳转后页面
    inventory_page.check_page_title()
    time.sleep(3)
    inventory_page.has_goods()