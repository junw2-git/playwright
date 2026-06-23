import pytest

def run_all():
    pytest.main([
        "-v",
        "tests/",
        "--html=reports/test_report.html",
        "--self-contained-html"
    ])


if __name__ == "__main__":
    run_all()
