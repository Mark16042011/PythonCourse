class Bus:
    def __init__(self, speed: float, capacity: int, max_speed: float, passengers: list, seats: dict):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = passengers
        self.seats = seats

    @property
    def __countOfEmptySeats(self) -> int:
        return self.capacity - len(self.passengers)

    @property
    def hasEmptySeats(self) -> bool:
        return self.__countOfEmptySeats > 0

    def __iadd__(self, other):
        if type(other) is str:
            if self.hasEmptySeats:
                self.passengers.append(other)
        elif self.hasEmptySeats:
            for item in other:
                if self.hasEmptySeats:
                    self.passengers.append(item)
        return self

    def __isub__(self, other):
        if type(other) is not str:
            for item in other:
                if item in self.passengers:
                    self.passengers.remove(item)
        elif type(other) is str:
            if other in self.passengers:
                self.passengers.remove(other)
        return self

    def __contains__(self, item: str):
        if item in self.passengers:
            return True
        else:
            return False


bus1 = Bus(23, 4, 35, ["peter", "oleg"], {1: "peter", 2: "oleg"})
bus1 += ["maxim", "sana"]
bus1 -= ["maxim", "oleg", "mark"]
print(bus1.passengers)
print("masha" in bus1)