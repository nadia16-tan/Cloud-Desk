
from flask import Flask, jsonify

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return "Welcome to CloudDesk!"

# API health check
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "application": "CloudDesk",
        "status": "running",
        "message": "CloudDesk API is working!"
    })

if __name__ == "__main__":
    app.run(debug=True)
