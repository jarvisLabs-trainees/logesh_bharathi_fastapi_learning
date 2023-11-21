from fastapi import FastAPI
from enum import Enum
import uvicorn

app = FastAPI()


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


if __name__ == "__main__":
    uvicorn.run(app, host="8.0.0.0", port=8080, reload=True)
