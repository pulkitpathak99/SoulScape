import requests
from config import Config

class GeminiClient:
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self.endpoint = "https://api.gemini.flash/analyze"  # Replace with Gemini endpoint

    def analyze_emotion(self, user_input):
        try:
            headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
            payload = {'text': user_input}
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get('response', "Sorry, I couldn't process your input.")
        except requests.exceptions.RequestException as e:
            print(f"Error with Gemini API: {e}")
            return "I'm having trouble connecting to the AI service. Please try again later."
