# tests/test_dashboard.py
from fastapi.testclient import TestClient
from dashboard.app import app

client = TestClient(app)

def test_stats():
    response = client.get("/stats")
    assert response.status_code == 200

def test_trace():
    response = client.get("/trace")
    assert response.status_code == 200

def test_errors():
    response = client.get("/errors")
    assert response.status_code == 200
