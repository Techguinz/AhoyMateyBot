
from flask import Flask, request, jsonify
from pymongo import MongoClient
import json


connectionString = "mongodb+srv://vivekrana775:12345@cluster0.yolwjkm.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connectionString)
dbs = client.list_database_names()

chatbot_db = client.chatbot
chatbot_collection = chatbot_db.Chatbot

app=Flask(__name__)

@app.route('/')
def home():
    return "Home"

@app.route('/get-intents')
def get_Intents():
    intents = chatbot_collection.find()
    intents = list(intents)
    json_data = json.dumps(intents)

    return Response(json_data, content_type='application/json')

    return "Help", 200

@app.route('/insert-intent',methods=["POST"])
def insertIntent():
    intent = request.get_json()
    chatbot_collection.insert_one(intent)
    return jsonify(intent), 201

def insertPlaind():
    return "Trej"

if __name__=="__main__":
    app.run(debug=True)