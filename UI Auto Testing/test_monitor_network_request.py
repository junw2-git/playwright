from playwright.sync_api import sync_playwright


def test_network_monitor():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        print("\n")

        def log_request(request):
            if "baidu" in request.url:
                print("请求-url:", request.url)
                print("请求-type:", request.resource_type)

        page.on("request", log_request)
        page.goto("https://www.baidu.com")

        browser.close()
