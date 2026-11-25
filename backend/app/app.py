
from flask import Flask, jsonify,request
from database import initialize_database,get_db_connection

app = Flask(__name__)

initialize_database()

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
    
    # Create a new support ticket
@app.route("/api/tickets", methods=["POST"]) 
def create_ticket():
    data=request.get_json()
    title=data.get("title")
    description=data.get("description")
    priority=data.get("priority")
    if not title or not description or not priority:
        return jsonify({"error":"All fields are required"}),400
    connection = get_db_connection()
       

if __name__ == "__main__":
    app.run(debug=True)
