
from flask import Flask, jsonify, request

from fitness_utils import calculate_bmi


app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "message": "Fitness management API is running"
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.post("/bmi")
def bmi():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    try:
        weight = float(data["weight_kg"])
        height = float(data["height_m"])
        result = calculate_bmi(weight, height)
    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Provide valid positive weight_kg and height_m values"
        }), 400

    return jsonify({"bmi": result}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
