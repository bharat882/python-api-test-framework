import requests
from src.config.settings import settings


class BaseClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.timeout = settings.TIMEOUT

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data, json=json, headers=headers, timeout=self.timeout)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, data=data, json=json, headers=headers, timeout=self.timeout)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers, timeout=self.timeout)
        return response