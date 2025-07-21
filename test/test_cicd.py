import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_population_success(client):
    response = client.get('/city/Paris/population')
    assert response.status_code == 200
    data = response.get_json()
    assert data["city"] == "Paris"
    assert isinstance(data["population"], int)

def test_area_success(client):
    response = client.get('/city/London/area')
    assert response.status_code == 200
    data = response.get_json()
    assert data["city"] == "London"
    assert isinstance(data["area_km2"], float)

def test_fun_fact_success(client):
    response = client.get('/city/Tokyo/fun-fact')
    assert response.status_code == 200
    data = response.get_json()
    assert data["city"] == "Tokyo"
    assert isinstance(data["fun_fact"], str)

def test_missing_city_path(client):
    response = client.get('/city//population')
    assert response.status_code == 404

def test_unknown_endpoint(client):
    response = client.get('/city/Berlin/history')
    assert response.status_code == 404
    assert response.get_json()["error"] == "Resource not found"
