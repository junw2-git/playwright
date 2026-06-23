'''
登录页 POM
'''
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

        self.username = "#user-name"
        self.password = "#password"
        self.login_btn = "#login-button"

    def load(self):
        self.page.goto(self.url)

    def input_username(self, text):
        self.page.fill(self.username, text)

    def input_password(self, text):
        self.page.fill(self.password, text)

    def click_login(self):
        self.page.click(self.login_btn)