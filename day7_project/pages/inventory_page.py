'''
商品列表
'''
class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_cart = "button:text('Add to cart')"
        self.cart_icon = ".shopping_cart_link"

    def add_first_item(self):
        self.page.locator(self.add_cart).nth(0).click()

    def add_second_item(self):
        self.page.locator(self.add_cart).nth(1).click()

    def go_to_cart(self):
        self.page.click(self.cart_icon)
