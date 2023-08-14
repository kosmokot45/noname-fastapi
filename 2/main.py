from fastapi import FastAPI
from data import users, users2, trades

app = FastAPI(title='2nd')


@app.get("/")
def hello():
    return "Hello!"

@app.get("/users/{user_id}")
def get_users(user_id: int):
    return [user for user in users if user.get("id") == user_id]

@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return trades[offset:][:limit]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}