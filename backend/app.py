from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from sentence_transformers import SentenceTransformer
import lancedb
import torch
from backend.setup import initialize_system
# from backend.services.db import save_user_data, save_answer_data
from backend.services.embedder import embed
import backend.services.rag as rag

app = Flask(__name__)
CORS(app)

llm_url = 'http://127.0.0.1:5000/ask'
initialize_system()

@app.route('/query-llm', methods=['POST'])
def query(): # query llm and output the response for user's query
    data = request.get_json()
    response = rag.generate_response(data)
    return jsonify({"response": response})

@app.route('/switch-session', methods=['POST'])
def switch_sessions(): # when switching over to a new session deleted information is cleared from disk
    data = request.get_json()
    rag.delete_session_data(data)

@app.route('/manage-personal-info', methods=['POST'])
def manage_personal_info(): # periodically called to delete information from personal_info table to maintain size
    data = request.get_json()
    return jsonify(rag.clear_personal_table(data))

@app.route('/extract-info', methods=['POST'])
def extract_info(): # extract query specific information as well as personal information from user's query
    data = request.get_json()
    extracted_info = rag.extract_info(data)
    return jsonify({"extracted_info": extracted_info})


# @app.route("/api/save_user", methods=["POST"])
# def save_user():
#     data = request.json  
#     result = save_user_data(data, 333)
#     return jsonify({"status": result})

# @app.route("/api/save_answer", methods=["POST"])
# def save_answer():
#     data = request.json  
#     result = save_answer_data(data, 333)
#     return jsonify({"status": result})

if __name__ == '__main__':
    app.run(port=3000, debug=True) # change port from llm_api