class Nikola:
    __slots__ = ["name", "age"]

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        if name != "Николай":
            self.name = "Я не " + name + ",а Николай"


person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)
print(person1.name)
print(person2.name)