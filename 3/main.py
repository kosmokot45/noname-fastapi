from typing import List
from fastapi import FastAPI, Request, status
from data import users, users2, f_trades
from models import Trade, User
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse

app = FastAPI(title='2nd')


# if user need valid error
@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.get("/users/{user_id}", response_model=List[User])
def get_users(user_id: int):
    return [user for user in users if user.get("id") == user_id]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return f_trades[offset:][:limit]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(
        filter(lambda user: user.get("id") == user_id, users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


@app.post("/trades")
def add_trades(trades: List[Trade]):
    f_trades.extend(trades)  # type: ignore
    return {"status": 200, "data": f_trades}
