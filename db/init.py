import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

from dotenv import dotenv_values


config = dotenv_values(".env")
project_id = config.get("FIRESTORE_PROJECT_ID")

cred = credentials.Certificate(json.loads(config.get("KEY_JSON")))
# cred = credentials.Certificate("key/key.json")

firebase_admin.initialize_app(cred, {
    'projectId': project_id,
})

db = firestore.client()
