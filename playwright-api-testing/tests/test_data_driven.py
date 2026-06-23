from utils.data_loader import load_json, load_csv
import re

def test_load_json():
    data = load_json("test_data.json")
    assert data["user"] == "standard_user"
    assert data["pwd"] == "secret_sauce"
    assert data["base_url"] == "https://www.saucedemo.com"

def test_load_csv():
    data = load_csv("test_data.csv")
    print('\n')
    print(data[0], '\n')
    print(data[1], '\n')
    print(data[2], '\n')
    assert len(data) > 0
