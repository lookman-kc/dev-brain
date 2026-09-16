from importlib.metadata import metadata

from app.config.settings import get_settings

project_metadata = metadata("DevBrain")


def test_root(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["service"] == project_metadata["Name"]
    assert data["version"] == project_metadata["Version"]
    assert data["environment"] == get_settings().app_env
    assert data["status"] == "ok"


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
