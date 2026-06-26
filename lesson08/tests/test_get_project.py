import uuid


def test_get_project_positive(project_api, created_project):

    title = "Project " + str(uuid.uuid4())

    project_id = created_project(title)

    response = project_api.get_project(project_id)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == project_id
    assert body["title"] == title


def test_get_project_wrong_id(project_api):

    response = project_api.get_project("999999999")

    assert response.status_code in (404, 400)
