import string
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(q: str):
    return {"message": q}
