"""
Pruebas unitarias e integración para la API usando pytest.
"""

import pytest
from backend.api_app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Prueba del endpoint raíz."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "mensaje" in data

def test_get_opiniones(client):
    """Prueba del endpoint de opiniones."""
    response = client.get("/api/opiniones/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_trending(client):
    """Prueba del endpoint de trending topics."""
    response = client.get("/api/trending/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list) 