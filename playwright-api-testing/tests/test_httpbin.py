from utils.assertions import assert_status_code

'''
API 基础测试
'''
def test_get_request(api_client):
    res = api_client.get("/get")
    assert_status_code(res, 200)

def test_post_request(api_client):
    res = api_client.post("/post", json={"name": "test"})
    assert_status_code(res, 200)
