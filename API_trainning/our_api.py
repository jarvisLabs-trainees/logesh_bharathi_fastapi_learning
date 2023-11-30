from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

@app.get("/wish")
async def GetWishes():
    result = requests.get("https://0610a604ee46d44915237e0bb9baeaa0.notebooksb.jarvislabs.net")
    return result.json();


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str

@app.post("/users/")
async def create_user(user_data: CreateUserRequest):
        result = requests.post("https://0610a604ee46d44915237e0bb9baeaa0.notebooksb.jarvislabs.net/users/",data=user_data.json())
        return result.json();
