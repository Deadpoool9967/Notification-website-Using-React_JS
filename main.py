from fastapi import FastAPI
from firebase import firebase
import random

app = FastAPI()

firebase = firebase.FirebaseApplication("https://web-notifere-default-rtdb.firebaseio.com/", None)
result = firebase.get('/messages', '')

@app.get('/')
async def root():
    return result

@app.get('/English')
async def root():
    data = result['English']
    new_array = [x for x in data if x is not None]
    
    mani = random.choice(new_array)
    return mani

@app.get('/Hindi')
async def root():
    data = result['Hindi']
    new_array = [x for x in data if x is not None]
    
    mani = random.choice(new_array)
    return mani