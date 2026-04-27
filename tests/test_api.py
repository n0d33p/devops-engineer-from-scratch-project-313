import pytest
from fastapi.testclient import TestClient
from main import app
from sqlmodel import Session, delete
from database import engine
from models import Link

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(autouse=True)
def clean_database():
    with Session(engine) as session:
        session.execute(delete(Link))
        session.commit()

def test_create_link(client):
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

def test_get_links(client):
    response = client.get("/api/links")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_one_link(client):
    item = client.post("/api/links", json={"original_url": "https://ya.ru", "short_name": "yandex"}).json()
    link_id = item["id"]

    response = client.get(f"/api/links/{link_id}")
    assert response.status_code == 200
    assert response.json()["short_name"] == "yandex"

def test_delete_link(client):
    item = client.post("/api/links", json={"original_url": "https://test.com", "short_name": "delete-me"}).json()
    link_id = item["id"]

    response = client.delete(f"/api/links/{link_id}")
    assert response.status_code == 204

    get_response = client.get(f"/api/links/{link_id}")
    assert get_response.status_code == 404

def test_links_with_pagination(client):
    for i in range(1, 6):
        client.post("/api/links", json={"original_url": f"https://site{i}.com", "short_name": f"name{i}"})
    response = client.get("/api/links?range=[0,2]")

    assert response.status_code == 200
    assert len(response.json()) == 3
    assert "Content-Range" in response.headers
    assert response.headers["Content-Range"] == "links 0-2/5"