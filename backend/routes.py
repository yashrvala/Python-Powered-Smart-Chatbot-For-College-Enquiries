from flask import Blueprint, request, jsonify
from chatbot_engine import get_response

api_bp = Blueprint('api', __name__)

@api_bp.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        answer = get_response(question)
        return jsonify({"answer": answer})
    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({"error": f"Server error: {str(e)}"}), 500
