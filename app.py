from flask import Flask, request, jsonify
from gemini_client.py import GeminiClient
from firebase_client import FirebaseClient
from config import Config
from datetime import datetime

# Initialize Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Gemini and Firebase Clients
gemini = GeminiClient()
firebase = FirebaseClient()

@app.route('/')
def home():
    return jsonify({"status": "up", "message": "Welcome to the Mental Wellness Chatbot!"})

# Save user mood data
@app.route('/save', methods=['POST'])
def save_data():
    try:
        data = request.json
        data['timestamp'] = datetime.utcnow().isoformat()
        firebase.save_user_data('user_moods', data)
        return jsonify({"status": "success", "message": "Data saved successfully."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Handle chat with Gemini API
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        if not user_message:
            return jsonify({"status": "error", "message": "Message cannot be empty."}), 400

        response_text = gemini.analyze_emotion(user_message)

        # Save conversation data
        firebase.save_user_data('user_conversations', {
            "user_message": user_message,
            "bot_response": response_text,
            "timestamp": datetime.utcnow().isoformat()
        })

        return jsonify({"response": response_text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
