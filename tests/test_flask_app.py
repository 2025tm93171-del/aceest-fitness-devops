
import pytest

from flask_app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["application"] == "ACEest Fitness & Gym"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_bmi_endpoint(client):
    response = client.post(
        "/bmi",
        json={"weight_kg": 70, "height_m": 1.75},
    )

    assert response.status_code == 200
    assert response.json["bmi"] == 22.86


def test_bmi_rejects_invalid_input(client):
    response = client.post(
        "/bmi",
        json={"weight_kg": 70, "height_m": 0},
    )

    assert response.status_code == 400
    assert "error" in response.json


def test_bmi_rejects_missing_input(client):
    response = client.post("/bmi", json={"weight_kg": 70})

    assert response.status_code == 400
