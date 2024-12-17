import os

class Config:
    # Gemini 2.0 Flash API Key
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'YOUR_API_KEY')

    # Firebase Credentials Path
    FIREBASE_CRED_PATH = os.getenv('FIREBASE_CRED_PATH', 'cred.json')

    # Flask Server Configuration
    DEBUG = os.getenv('DEBUG', True)
    HOST = '0.0.0.0'
    PORT = 5000
