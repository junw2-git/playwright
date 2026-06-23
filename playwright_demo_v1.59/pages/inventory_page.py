import time

from pages.base_page import BasePage


class InventoryPage(BasePage):
    # 页面元素
    TITLE = ".title"
    ITEM_LIST = ".inventory_item"

    # 校验页面标题
    def check_page_title(self):
        self.assert_text(self.TITLE, "Products")

    time.sleep(3)

    # 判断商品列表是否加载
    def has_goods(self):
        # debug is always failed
        # self.wait_for_visible(self.ITEM_LIST)
        # 额外校验至少存在1个商品
        print("Shops Number is:", self.page.locator(self.ITEM_LIST).count())
        assert self.page.locator(self.ITEM_LIST).count() > 0, "页面无商品"
