import firebase_admin
from firebase_admin import credentials,db

URL = 'https://learning-py-72e9c-default-rtdb.firebaseio.com/'

firebase_sdk = credentials.Certificate('learning-py-72e9c-firebase-adminsdk-8dzec-ba463cf03a.json')
firebase_admin.initialize_app(firebase_sdk,{'databaseURL': URL})

ref = db.reference('/Usuarios')
ref.push({'Juan':'1234','Diego':'0000'})