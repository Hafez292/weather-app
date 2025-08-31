from flask import Flask, jsonify, request
import requests


app = Flask(__name__)
API_KEY = "064b26e7392a4f7b906164332250808"


@app.route('/weather')
def get_weather():
    # Get city from URL parameters
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "Please provide a city parameter"}), 400

    city_name = city.lower()
    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={city_name}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "city": city.capitalize(),
            "temperature": f"{data['current']['temp_c']}°C",
            "wind_speed": f"{data['current']['wind_kph']} km/h",
            "condition": data['current']['condition']['text'].capitalize()
        })
    else:
        return jsonify({"error": f"Weather data not found for {city}"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
