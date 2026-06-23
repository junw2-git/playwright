from pages.base_page import BasePage

class LoginPage(BasePage):
    # 页面元素定位器
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BTN = "#login-button"

    # 登录业务方法
    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)