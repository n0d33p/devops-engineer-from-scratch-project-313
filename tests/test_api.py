import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_link():
    payload = {
        "original_url": "https://google.com",
        "short_name": "google"
    }
    response = client.post("/api/links", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["short_name"] == "google"
    assert "id" in data
    assert "short_url" in data

def test_get_links():
    response = client.get("/api/links")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_one_link():
    item = client.post("/api/links", json={"original_url": "https://ya.ru", "short_name": "yandex"}).json()
    link_id = item["id"]

    response = client.get(f"/api/links/{link_id}")
    assert response.status_code == 200
    assert response.json()["short_name"] == "yandex"

def test_delete_link():
    item = client.post("/api/links", json={"original_url": "https://test.com", "short_name": "delete-me"}).json()
    link_id = item["id"]

    response = client.delete(f"/api/links/{link_id}")
    assert response.status_code == 204

    get_response = client.get(f"/api/links/{link_id}")
    assert get_response.status_code == 404