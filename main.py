from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

user = {
    "name": "Ram",
    "age": 20
}

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def get_user():
    return user

@app.put("/user")
def update_user(updated_user: User):
    user["name"] = updated_user.name
    user["age"] = updated_user.age
    return {
        "message": "User Updated Successfully",
        "user": user
    }