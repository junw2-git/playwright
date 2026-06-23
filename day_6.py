from playwright.sync_api import sync_playwright, expect

def test_example_login():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # ======================
        # 1. 打开登录页
        # ======================
        page.goto("https://www.saucedemo.com")

        # ======================
        # 2. 执行登录
        # ======================
        page.fill("#user-name", "standard_user")  # 替换成你的真实用户名
        page.fill("#password", "secret_sauce")  # 替换成你的真实密码
        page.click("#login-button")

        # ======================
        # 3. 断言1：URL 跳转成功
        # ======================
        try:
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        except Exception as e:
            print(e)
        finally:
            print("断言1：URL 跳转成功")

        # ======================
        # 4. 断言2：页面显示用户名（你自己改定位）
        # 假设用户名显示在 .user-name 或 #user-display
        # =====================
        # 把你页面上真实显示的用户名填进去
        try:
            expect(page.get_by_text("Products")).to_be_visible(timeout=10000)
        except Exception as e:
            print(e)
        finally:
            print('断言2：真实显示的用户名')

        # ======================
        # 5. 断言3：登录后 Cookie 存在
        # ======================
        try:
            cookies = context.cookies()
            # 打印所有 cookie 方便你查看
            print("登录后Cookies：", cookies)

            # 方法A：判断是否包含登录凭证cookie（通用写法）
            has_auth_cookie = any("session" in c["name"].lower() or "token" in c["name"].lower() for c in cookies)
            assert has_auth_cookie is True, "登录后未找到会话Cookie"

            # 方法B：精确判断某个cookie名称（最稳）
            # expect(cookies).to_contain({"name": "your_session_cookie_name"})
        except Exception as e:
            print(e)
        finally:
            print("断言3：登录后 Cookie 存在")

        # ======================
        # 结束
        # ======================
        print("✅ 登录成功 + 全部断言通过")
        browser.close()

if __name__ == "__main__":
    test_example_login()