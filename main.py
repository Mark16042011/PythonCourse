from fastapi import FastAPI

app = FastAPI()


@app.post("/names")
def new_name(name: str):
    file = open("names", "a")
    file.write(name + "\n")
    file.close()
    return "ok"


@app.delete("/names")
def delete_name(name: str):
    file = open("names", "r")
    for item in file:
        if item != name:
            file = open("names", "a")
            file.write(item)
    return file

#
# @app.get("/names")
# def get_names():
#     list_of_names = open("/", "r")
#     return list_of_names
