from flask import Blueprint, request, jsonify

from app.services.rag_service import ask_question


chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:

        return jsonify({
            "error": "Question is required"
        }), 400

    try:

        result = ask_question(question)

        return jsonify(result)

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500