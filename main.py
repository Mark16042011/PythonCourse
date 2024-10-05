import json

from fastapi import FastAPI, HTTPException

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
    # TODO: add id
    new_user = {
        "name": name,
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
def delete_name(name: str):
    file = open("names.txt", "r")
    new_names = []
    for item in file:
        if item.replace('\n', '') != name:
            new_names.append(item)
    file.close()

    file = open("names.txt", "w")
    for item in new_names:
        file.write(item)
    file.close()

    return new_names


@app.get("/names")
def get_names():
    file = open("names.txt", "r")
    names = []
    for item in file:
        names.append(item)
    file.close()
    return names
