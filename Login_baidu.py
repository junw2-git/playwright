import time

from playwright.sync_api import sync_playwright, expect


def run_baidu_map():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        # 1. 打开百度
        page.goto("https://www.baidu.com")
        print("✅ 打开百度成功")

        # 1. 先“埋伏”，准备接收新标签页
        with context.expect_page() as new_page_info:
            page.locator('//*[@id="s-top-left"]/a[3]').click()
            print("✅ 已点击地图")

        # 2. 拿到新标签页对象
        new_tab = new_page_info.value
        new_tab.wait_for_load_state("networkidle")  # 等加载稳定

        # 4. 在新标签页上断言 URL
        # option 1)
        expect(new_tab).to_have_url(r"https://map.baidu.com/@13058459,3702796,15z")
        # option 2)
        assert "map.baidu.com" in new_tab.url, "新标签页 URL 不对"
        print("✅ 成功跳转到百度地图！")

        # 3. 点“路线”按钮（进入路线面板）
        # 定位：搜索框右边的“路线”按钮
        new_tab.locator(".route-button").click()
        new_tab.wait_for_selector(".route-searchbox-content", state="visible")
        print("✅ 打开路线面板")

        # 4. 在【起点输入框】写入“保利海上五月花二期”
        # 路线面板里第一个输入框（起点）
        start_input = new_tab.locator(".route-searchbox-content input").nth(0)
        start_input.click()
        start_input.fill(start_address)
        print("✅ 起点输入框已写入:", start_address)

        # 5. 在【输入终点】写入“包孝肃公祠”
        # 路线面板里第二个输入框（终点）
        end_input = new_tab.locator(".route-searchbox-content input").nth(1)
        end_input.click()
        end_input.fill(end_address)
        print("✅ 终点输入框已写入:", end_address)

        # （可选）验证输入值
        expect(start_input).to_have_value(start_address)
        print("✅ 验证起点输入正确")
        expect(end_input).to_have_value(end_address)
        print("✅ 验证终点输入正确")

        time.sleep(3)

        # click search button
        new_tab.click("#search-button")
        time.sleep(10)
        print("✅ 搜素完成")

        browser.close()


if __name__ == "__main__":
    start_address = "保利海上五月花-B区"
    end_address = "凤阳县临淮关镇政府"
    run_baidu_map()
