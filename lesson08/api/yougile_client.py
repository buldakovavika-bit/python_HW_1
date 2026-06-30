import requests

from lesson08.conftest import BASE_URL, HEADERS


class ProjectApi:

    def __init__(self):
        self.url = f"{BASE_URL}/projects"

    def create_project(self, body):
        return requests.post(
            self.url,
            json=body,
            headers=HEADERS
        )

    def delete_project(self, project_id: str):
        return requests.delete(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.HEADERS
        )


class YouGileClient:

    def setup_method(self):
        self.project_api = ProjectApi()

    def create_project(self, title: str):
        payload = {"title": title}
        response = requests.post(
            f"{self.BASE_URL}/projects",
            json=payload,
            headers=self.HEADERS
        )
        return response

    def update_project(self, project_id: str, payload: dict):
        response = requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            json=payload,
            headers=self.HEADERS
        )
        return response

    def delete_project(self, project_id: str):
        return requests.delete(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.HEADERS
        )
