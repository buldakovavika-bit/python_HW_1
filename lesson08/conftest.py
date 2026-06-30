import pytest
from api.project_api import ProjectAPI
from config import TOKEN


@pytest.fixture
def project_api():
    return ProjectAPI(TOKEN)


@pytest.fixture
def created_project(project_api):
    """
    Создает проект перед тестом
    и удаляет его после завершения теста.
    """

    project_ids = []

    def _create(title):
        response = project_api.create_project(title)
        assert response.status_code == 201

        project_id = response.json()["id"]
        project_ids.append(project_id)

        return project_id

    yield _create

    for project_id in project_ids:
        project_api.delete_project(project_id)
