import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("messattendance-fc208-firebase-adminsdk-rhjmd-b454daa2e4.json")
firebase_admin.initialize_app(cred)



db=firestore.client()


