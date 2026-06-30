import uuid


def test_create_project_positive(project_api, created_project):

    title = "Project " + str(uuid.uuid4())

    project_id = created_project(title)

    response = project_api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["title"] == title


def test_create_project_negative(project_api):

    response = project_api.create_project("")

    assert response.status_code == 400

    assert "error" in response.text.lower()
