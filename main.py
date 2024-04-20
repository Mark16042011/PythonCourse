class Bus:
    def __init__(self, speed: float, capacity: int, max_speed: float, passengers: list, seats: dict):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = passengers
        self.seats = seats

    # TODO: убрать пересчет has_empty_seats из каждого места, пускай оно считается в моменте отдельным проперти
    # количество пустых мест в автобусе
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

    # def __isub__(self, other):
    #     if self.has_empty_seats:
    #         if type(other) is str:
    #             for item in other:
    #                 if self.has_empty_seats:
    #                     self.passengers.remove(item)
    #                     if len(self.passengers) == self.capacity:
    #                         self.has_empty_seats = False
    #                     else:
    #                         self.has_empty_seats = True
    #         elif self.has_empty_seats:
    #             self.passengers.remove(other)
    #             if len(self.passengers) == self.capacity:
    #                 self.has_empty_seats = False
    #             else:
    #                 self.has_empty_seats = True


bus1 = Bus(23, 4, 35, ["peter", "oleg"], {1: "peter", 2: "oleg"})
bus1 += ["maxim", "sana"]
# bus1 -= "maxim"
print(bus1.passengers)
