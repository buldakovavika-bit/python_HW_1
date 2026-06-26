from api.client import ApiClient


class ProjectAPI:

    def __init__(self, token):
        self.client = ApiClient(token)

    def create_project(self, title):
        body = {
            "title": title
        }
        return self.client.post("/projects", body)

    def update_project(self, project_id, title):
        body = {
            "title": title
        }
        return self.client.put(f"/projects/{project_id}", body)

    def get_project(self, project_id):
        return self.client.get(f"/projects/{project_id}")

    def delete_project(self, project_id):
        return self.client.delete(f"/projects/{project_id}")
