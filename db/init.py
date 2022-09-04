import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from dotenv import dotenv_values


def main():
    config = dotenv_values(".env")
    project_id = config.get("FIRESTORE_PROJECT_ID")

    cred = credentials.Certificate("key/key.json")
    firebase_admin.initialize_app(cred, {
        'projectId': project_id,
    })

    db = firestore.client()

    return db
