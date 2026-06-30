import requests
from config import BASE_URL


class ApiClient:

    def __init__(self, token):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def post(self, endpoint, body):
        return requests.post(
            self.base_url + endpoint,
            json=body,
            headers=self.headers
        )

    def put(self, endpoint, body):
        return requests.put(
            self.base_url + endpoint,
            json=body,
            headers=self.headers
        )

    def get(self, endpoint):
        return requests.get(
            self.base_url + endpoint,
            headers=self.headers
        )

    def delete(self, endpoint):
        return requests.delete(
            self.base_url + endpoint,
            headers=self.headers
        )
