import json
from lib2to3.pytree import NodePattern
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import Field, BaseModel

app = FastAPI()


@app.post("/names")
def new_name(name: str, date_of_birth: str):
    file = open("data.json", "r")
    data: dict = json.load(file)
    file.close()

    users: list[dict] = data.get('users', [])
    for user in users:
        temp_name = user.get('name')
        if temp_name == name:
            # Если пользователь с таким именем уже существует, то прокидываем ошибку
            raise HTTPException(status_code=418, detail="User with this name already exist")

    biggest_id = 0
    for user in users:
        id = user.get("id")
        if id > biggest_id:
            biggest_id = id
    biggest_id = biggest_id + 1

    new_user = {
        "name": name,
        'id': biggest_id,
        "date_of_birth": date_of_birth
    }
    users.append(new_user)
    new_data = {
        "users": users
    }

    file = open("data.json", "w")
    file.write(json.dumps(new_data, indent=2))
    file.close()

    return new_user


@app.delete("/names")
def delete_user(name: str):
    file = open("data.json", "r")
    data: dict = json.load(file)
    new_users = []
    users: list[dict] = data.get("users", [])
    for user in users:
        if user.get("name") != name:
            new_users.append(user)
    print(new_users)

    file.close()

    new_data = {
        "users": new_users
    }
    file = open("data.json", "w")
    file.write(json.dumps(new_data, indent=2))
    file.close()

    return new_users


@app.get("/names")
def get_names():
    file = open("data.json", "r")
    data: dict = json.load(file)
    users = data.get("users")

    return users


@app.put("/names")
def update_user(id: int, name: str = None, date_of_birth: str = None):
    file = open("data.json", "r")
    data: dict = json.load(file)
    file.close()
    users: list[dict] = data.get("users")

    for user in users:
        if user.get('id') == id:
            user.update({"name": name if name else user.get("Name"),
                         "date_of_birth": date_of_birth if date_of_birth else user.get("date_of_birth")})

            file = open("data.json", "w")
            file.write(json.dumps({"users": users}, indent=2))
            file.close()

            return user

    raise HTTPException(status_code=404)
