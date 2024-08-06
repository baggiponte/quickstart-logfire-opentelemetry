from fastapi import FastAPI
import logfire

from roll import roll

logfire.configure()


app = FastAPI()

logfire.instrument_fastapi(app)


@app.get("/roll")
async def diceroll():
    result = str(roll())
    return {"number": result}


@app.get("/")
async def root():
    return {"message": "Hello World"}
