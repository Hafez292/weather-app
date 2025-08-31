from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get API key from environment variable or use default
API_KEY = os.environ.get("WEATHER_API_KEY", "064b26e7392a4f7b906164332250808")

@app.route('/weather')
def get_weather():
    # Get city from URL parameters
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "Please provide a city parameter"}), 400

    city_name = city.lower()
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        return jsonify({
            "city": data['location']['name'],
            "country": data['location']['country'],
            "temperature": f"{data['current']['temp_c']}°C",
            "feels_like": f"{data['current']['feelslike_c']}°C",
            "wind_speed": f"{data['current']['wind_kph']} km/h",
            "wind_direction": data['current']['wind_dir'],
            "humidity": f"{data['current']['humidity']}%",
            "condition": data['current']['condition']['text'],
            "icon": data['current']['condition']['icon'],
            "last_updated": data['current']['last_updated']
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch weather data: {str(e)}"}), 500
    except (KeyError, ValueError) as e:
        return jsonify({"error": f"Unexpected data format from weather service"}), 500

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "weather-api"})

if __name__ == "__main__":
    print("Starting Weather API Server...")
    print("API Key:", "*" * len(API_KEY) if API_KEY else "Not set")
    app.run(host='0.0.0.0', port=5050, debug=True)