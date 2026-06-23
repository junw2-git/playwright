import re
from playwright.sync_api import Page, expect

# 打开首页，确认标题正确
def test_has_title(page: Page):
    page.goto("https://www.sunzhongwei.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("大象笔记"))

# 点击关于我链接，确认跳转正确
def test_get_started_link(page: Page):
     page.goto("https://www.sunzhongwei.com/")

     #Click the about me link.
     page.get_by_role("link", name="关于我").click()

     #Expects page to have a heading with the name of About Me.
     expect(page.get_by_role("heading", name="自建博客")).to_be_visible()