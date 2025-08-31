import pytest
from weather import app
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_missing_city_parameter(client):
    """Test missing city parameter"""
    response = client.get('/weather')
    assert response.status_code == 400
    assert b"Please provide a city parameter" in response.data


def test_valid_weather_request(client, requests_mock):
    """Test successful weather API response"""
    # Mock the external API response
    mock_response = {
        "current": {
            "temp_c": 22,
            "wind_kph": 15,
            "condition": {"text": "Sunny"}
        }
    }
    requests_mock.get(
        "http://api.weatherapi.com/v1/current.json?key=064b26e7392a4f7b906164332250808&q=london",
        json=mock_response
    )

    response = client.get('/weather?city=London')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data == {
        "city": "London",
        "temperature": "22°C",
        "wind_speed": "15 km/h",
        "condition": "Sunny"
    }


def test_api_failure(client, requests_mock):
    """Test weather API failure scenario"""
    requests_mock.get(
        "http://api.weatherapi.com/v1/current.json?key=064b26e7392a4f7b906164332250808&q=invalid",
        status_code=404
    )

    response = client.get('/weather?city=invalid')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert "not found for invalid" in data["error"]


def test_lowercase_city_conversion(client, requests_mock):
    """Test city name case insensitivity"""
    requests_mock.get(
        "http://api.weatherapi.com/v1/current.json?key=064b26e7392a4f7b906164332250808&q=paris",
        json={"current": {"temp_c": 18, "wind_kph": 10, "condition": {"text": "Cloudy"}}}
    )

    response = client.get('/weather?city=PARIS')
    assert response.status_code == 200