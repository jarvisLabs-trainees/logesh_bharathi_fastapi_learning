from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from gtts import gTTS;
import os;


app = FastAPI()

#here i am trying to practice Get api 
@app.get("/")
def index():
    return {"msg": "Hello world"}


@app.get("/about")
def about():
    return {"msg": "Naan thaan logesh"}


@app.get("/about/{id}")
def about_id(id: int):
    return {"msg": "Hello world", "id": id}


class UserId(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/user/{id}")
def user_id(id: UserId):
    return {"msg": "Hello world", "id": id}




class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str

@app.post("/users/")
async def create_user(user_data: CreateUserRequest):
       return {"message": "User created successfully", "user_data": user_data.dict()}

class Sentence(BaseModel):
    name: str

def text_to_speech(sentence:str):
    tts = gTTS(text=sentence, lang='en',tld="com.br")
    tts.save("output.mp3")
    os.system("open output.mp3");
  

    

@app.post("/speaker")
async def speaker_api(sentence: Sentence):
    text_to_speech("hello " + sentence.name)
    return "Success";
