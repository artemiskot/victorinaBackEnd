from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pymongo
import json
import random
from pymongo import cursor

client = pymongo.MongoClient("mongodb+srv://adming:0WatQ33l94AUHYp4@victorinazhivotnie.wkqdr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["victorinaZhivotnie"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/nameById")
async def getnameById(id: int):
    res = []
    cursor = db.question
    for i in cursor.find({'id': id}):
        res.append({"name": i['name']})
    return res

@app.get("/pictureById")
async def getpictureById(id: int):
    res = []
    cursor = db.question
    for i in cursor.find({'id': id}):
        res.append({"picture": i['picture'][:10]})
    return res

@app.get("/soundById")
async def getsoundById(id: int):
    res = []
    cursor = db.question
    for i in cursor.find({'id': id}):
        res.append({"sound": i['sound'][:10]})
    return res

@app.get("/descriptionById")
async def descriptionById(id: int):
    res = []
    cursor = db.question
    for i in cursor.find({'id': id}):
        res.append({"sound": i['sound'][:10]})
    return res

@app.get("/allQuestions")
async def allQuestions():
    res = []
    cursor = db.question
    for i in cursor.find({}, {'_id': 0}):
        res.append(i)
    return res

@app.get("/getAnimal")
async def getAnimal():
    response = db.question.find_one({"id": random.randint(1,db.question.count())})
    result = {}
    result["id"] = response["id"]
    result["name"] = response["name"]
    result["picture"] = response["picture"]
    result["sound"] = response["sound"]
    result["description"] = response["description"]
    return result