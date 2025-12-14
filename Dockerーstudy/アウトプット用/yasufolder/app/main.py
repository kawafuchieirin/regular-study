from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import random
from datetime import datetime

app = FastAPI()

# docker-compose のサービス名 mongo に接続
client = MongoClient("mongodb://mongo:27017")
db = client.janken_db
matches = db.matches  # 1戦ごとのログ

HANDS = ["rock", "scissors", "paper"]  # グー/チョキ/パー（英語で統一）
WIN_MAP = {
    ("rock", "scissors"),
    ("scissors", "paper"),
    ("paper", "rock"),
}

class JankenRequest(BaseModel):
    player: str
    hand: str  # "rock" | "scissors" | "paper"

def judge(player_hand: str, cpu_hand: str) -> str:
    if player_hand == cpu_hand:
        return "draw"
    if (player_hand, cpu_hand) in WIN_MAP:
        return "win"
    return "lose"

@app.post("/janken")
def play(req: JankenRequest):
    if req.hand not in HANDS:
        return {"error": "hand must be one of rock/scissors/paper"}

    cpu_hand = random.choice(HANDS)
    result = judge(req.hand, cpu_hand)

    doc = {
        "player": req.player,
        "player_hand": req.hand,
        "cpu_hand": cpu_hand,
        "result": result,
        "created_at": datetime.utcnow(),
    }
    insert = matches.insert_one(doc)

    return {
        "id": str(insert.inserted_id),
        "player": req.player,
        "player_hand": req.hand,
        "cpu_hand": cpu_hand,
        "result": result,
    }

@app.get("/stats")
def stats():
    total = matches.count_documents({})
    wins = matches.count_documents({"result": "win"})
    loses = matches.count_documents({"result": "lose"})
    draws = matches.count_documents({"result": "draw"})
    win_rate = (wins / total) if total > 0 else 0.0

    return {
        "total": total,
        "win": wins,
        "lose": loses,
        "draw": draws,
        "win_rate": win_rate,
    }

@app.get("/ranking")
def ranking():
    pipeline = [
        {"$match": {"result": "win"}},
        {"$group": {"_id": "$player", "wins": {"$sum": 1}}},
        {"$sort": {"wins": -1}},
        {"$limit": 5},
    ]
    rows = list(matches.aggregate(pipeline))
    return [{"player": r["_id"], "wins": r["wins"]} for r in rows]
