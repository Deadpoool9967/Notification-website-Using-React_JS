from fastapi import FastAPI
from firebase import firebase

import random

firebase = firebase.FirebaseApplication("https://web-notifere-default-rtdb.firebaseio.com/", None)
result = firebase.get('/messages', '')

app = FastAPI()

@app.get('/')
async def root():
    return result




