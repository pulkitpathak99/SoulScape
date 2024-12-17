import firebase_admin
from firebase_admin import credentials, firestore
from config import Config

class FirebaseClient:
    def __init__(self):
        try:
            self.cred = credentials.Certificate(Config.FIREBASE_CRED_PATH)
            firebase_admin.initialize_app(self.cred)
            self.db = firestore.client()
        except Exception as e:
            raise Exception(f"Firebase initialization failed: {e}")

    def save_user_data(self, collection_name, data):
        try:
            self.db.collection(collection_name).add(data)
            print(f"Data successfully saved to Firestore: {data}")
        except Exception as e:
            raise Exception(f"Failed to save data to Firestore: {e}")
