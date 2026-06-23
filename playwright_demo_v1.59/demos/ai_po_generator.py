import os
from datetime import datetime


def generate_po_code():
    # 模拟根据页面元素生成 PO 代码
    po_code = '''
from pages.base_page import BasePage

class DemoPage(BasePage):
    INPUT = "#demo-input"
    BTN = "#demo-btn"
'''
    # 写入 reports 目录
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)

    file_name = f"po_prompt_{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
    file_path = os.path.join(report_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("# AI 自动生成 PO 代码\n```python\n" + po_code + "\n```")
    print(f"PO 文件已生成：{file_path}")


if __name__ == "__main__":
    generate_po_code()
