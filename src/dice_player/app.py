import httpx
from fastapi import FastAPI
from pydantic import BaseModel
import logfire

logfire.configure()

app = FastAPI()

logfire.instrument_fastapi(app)


class MyPayload(BaseModel):
    name: str
    age: int


@app.get("/play")
async def play(player: str | None = None):
    dice1_res = roll_dice_call()
    dice2_res = roll_dice_call()

    s = dice1_res + dice2_res
    is_winner = s == 7 or s == 11

    return {"player": player, "result": s, "is_winner": is_winner}


@app.get("/")
async def root():
    return {"message": "Welcome to dice player!"}


@app.post("/prova")
def prova(pyload: MyPayload):
    print(pyload.dict())
    return {"message": "Welcome to dice player!"}


def roll_dice_call() -> int:
    with httpx.Client() as client:
        resp = client.get("http://dice-roller:8080/roll")

    return resp.json()["number"]
