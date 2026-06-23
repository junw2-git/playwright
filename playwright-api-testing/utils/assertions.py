def assert_status_code(response, expected):
    assert response.status_code == expected, f"期望状态码: {expected}, 实际: {response.status_code}"


def assert_json_key(response, key, value=None):
    json_data = response.json()
    assert key in json_data, f"关键字 {key} 不存在"
    if value:
        assert json_data[key] == value, f"{key}值不匹配"
