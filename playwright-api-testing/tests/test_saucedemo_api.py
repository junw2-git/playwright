'''
接口抓包
'''
import re

def test_saucedemo_network(page):
    page.goto("https://www.saucedemo.com/")
    pattern = re.compile(r".*saucedemo\.com.*")

    with page.expect_response(pattern) as req:
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

    requests = req.value
    print('\n')
    print('-' * 20)
    print("URL: ", requests.url)
    print("Status: ", requests.status)
    print('-' * 20)
    assert requests.url != ""
    assert requests.status == 200

