from fastapi import FastAPI, Query
from pymongo import MongoClient
import random

app = FastAPI()

client = MongoClient("mongodb://mongo:27017")
db = client.topic_db
collection = db.topics


@app.post("/topics")
def create_topic(text: str, category: str):
    result = collection.insert_one({
        "text": text,
        "category": category,
        "used_count": 0
    })
    return {"id": str(result.inserted_id)}


@app.get("/topics/random")
def random_topic(category: str | None = Query(default=None)):
    query = {}
    if category:
        query["category"] = category

    topics = list(collection.find(query))
    if not topics:
        return {"error": "topic not found"}

    topic = random.choice(topics)

    collection.update_one(
        {"_id": topic["_id"]},
        {"$inc": {"used_count": 1}}
    )

    return {
        "id": str(topic["_id"]),
        "text": topic["text"],
        "category": topic["category"],
        "used_count": topic["used_count"] + 1
    }


@app.get("/topics/ranking")
def topic_ranking():
    topics = collection.find().sort("used_count", -1).limit(5)
    return [
        {
            "id": str(t["_id"]),
            "text": t["text"],
            "used_count": t["used_count"]
        }
        for t in topics
    ]