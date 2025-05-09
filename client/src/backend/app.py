from flask import Flask, request, jsonify
from flask_cors import CORS
from db import save_user_data, save_answer_data

app = Flask(__name__)
CORS(app)

@app.route("/api/save_user", methods=["POST"])
def save_user():
    data = request.json  
    result = save_user_data(data, 333)
    return jsonify({"status": result})

@app.route("/api/save_answer", methods=["POST"])
def save_answer():
    data = request.json  
    result = save_answer_data(data, 333)
    return jsonify({"status": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
