'''
购物车
'''
class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = ".cart_item"

    def get_item_count(self):
        return self.page.locator(self.cart_items).count()
