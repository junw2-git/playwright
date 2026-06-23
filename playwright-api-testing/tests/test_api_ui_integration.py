'''
接口 + UI 联动
'''
def test_ui_api_integration(page, api_client):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    res = api_client.get(path="/get")
    print('-' * 20)
    print("status_code:", res.status_code)
    print('-' * 20)
    assert res.status_code == 200
