import uuid


def test_update_project_positive(project_api, created_project):

    project_id = created_project("Old name")

    new_title = "New " + str(uuid.uuid4())

    response = project_api.update_project(project_id, new_title)

    assert response.status_code == 200

    response = project_api.get_project(project_id)

    assert response.json()["title"] == new_title


def test_update_project_wrong_id(project_api):

    response = project_api.update_project(
        "123456789",
        "New"
    )

    assert response.status_code in (400, 404)
