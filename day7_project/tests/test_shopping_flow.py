import json
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def load_data():
    path = os.path.join(os.path.dirname(__file__), "../data/login_data.json")
    with open(path, 'r', encoding="utf-8") as f:
        return json.load(f)


def test_shopping_flow(page):
    # 加载数据
    data = load_data()
    user = data["username"]
    pwd = data["password"]

    # 登录
    login = LoginPage(page)
    login.load()
    login.input_username(user)
    login.input_password(pwd)
    login.click_login()

    # 加商品
    inventory = InventoryPage(page)
    inventory.add_first_item()
    inventory.add_second_item()
    inventory.go_to_cart()

    # 断言购物车有商品
    cart = CartPage(page)
    count = cart.get_item_count()
    print('-' * 10)
    print('Count Number is:', count)
    print('-' * 10)
    assert count >= 2


if __name__ == "__main__":
    test_shopping_flow()
