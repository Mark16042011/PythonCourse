from fastapi import FastAPI

app = FastAPI()


@app.post("/names")
def new_name(name: str):
    file = open("names.txt", "a")
    file.write(name + "\n")
    file.close()
    return "ok"


@app.delete("/names")
def delete_name(name: str):
    file = open("names.txt", "r")
    new_names = []
    for item in file:
        if item != name:
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
