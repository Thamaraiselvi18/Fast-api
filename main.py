from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

user = {
    "name": "Ram",
    "age": 20
}

class User(BaseModel):
    name: str
    dept: str

@app.get("/")
def get_user():
    return user

@app.put("/user")
def update_user(updated_user: User):
    user["name"] = updated_user.name
    return {
        "message": "User Updated Successfully",
        "user": user
    }

@app.put("/user/dept")
def update_user(updated_user: User):
    user["dept"] = updated_user.dept
    return {
        "message": "User Department Updated Successfully",
        "user": user
    }