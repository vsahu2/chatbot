from flask import Flask, jsonify

app = Flask(__name__)

CITY_DATA = {
    "delhi": {
        "recycling_centers": ["GreenHub CP", "EcoStation Nehru Place"],
        "air_quality": {"aqi": 178, "status": "Moderate"}
    },
    "mumbai": {
        "recycling_centers": ["Recycle Mumbai", "EcoPoint Dadar"],
        "air_quality": {"aqi": 120, "status": "Good"}
    }
}

@app.route('/city/<city_name>')
def city_info(city_name):
    return jsonify(CITY_DATA.get(city_name.lower(), {"message": "No data available"}))

if __name__ == '__main__':
    app.run(port=5001)
