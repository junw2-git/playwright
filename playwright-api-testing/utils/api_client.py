import requests

class ApiClient:
    def __init__(self):
        self.base_url = "https://httpbin.ceshiren.com/"

    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        return requests.get(url, params=params)

    def post(self, path, data=None, json=None):
        url = f"{self.base_url}{path}"
        return requests.post(url, data=data, json=json)