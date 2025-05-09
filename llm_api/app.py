from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# ✅ 选择你想用的模型（建议用支持对话的 Instruct 模型）
HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"
HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_id = data.get("user_id")
    
    # context = data.get("context", "")

    full_prompt = data.get("prompt")

    payload = {
        "inputs": full_prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            answer = result[0]["generated_text"]
        else:
            answer = "Model did not return a valid response."

        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
