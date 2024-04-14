class Bus:
    def __init__(self, speed: float, capacity: int, max_speed: float, passengers: list, seats: dict):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = passengers
        self.seats = seats
        self.has_empty_seats: bool
        if len(self.passengers) == self.capacity:
            self.has_empty_seats = False
        else:
            self.has_empty_seats = True

    def landing_or_disembarkation(self, names: list, operation: str):
        if operation == "disembarkation":
            for name in names:
                self.passengers.remove(name)
        elif operation == "landing" and self.has_empty_seats:
            for name in names:
                if len(self.passengers) == self.capacity:
                    self.has_empty_seats = False
                else:
                    self.has_empty_seats = True
                    if self.has_empty_seats:
                        self.passengers.append(name)
        if len(self.passengers) == self.capacity:
            self.has_empty_seats = False
        else:
            self.has_empty_seats = True
        print(self.passengers)

    def speed_boost_or_decline(self, value: int, operation: str):
        if operation == "Boost" and self.speed + value <= self.max_speed:
            self.speed += value
        elif operation == "Decline" and self.speed - value >= 0:
            self.speed -= value
        print(self.speed)

    def __iadd__(self, other):
        if self.has_empty_seats:
            if type(other) is str:
                for item in other:
                    if self.has_empty_seats:
                        self.passengers.append(item)
                        if len(self.passengers) == self.capacity:
                            self.has_empty_seats = False
                        else:
                            self.has_empty_seats = True
            elif self.has_empty_seats:
                self.passengers.append(other)
                if len(self.passengers) == self.capacity:
                    self.has_empty_seats = False
                else:
                    self.has_empty_seats = True
            print(self.passengers)

    def __isub__(self, other):
        if self.has_empty_seats:
            if type(other) is str:
                for item in other:
                    if self.has_empty_seats:
                        self.passengers.remove(item)
                        if len(self.passengers) == self.capacity:
                            self.has_empty_seats = False
                        else:
                            self.has_empty_seats = True
            elif self.has_empty_seats:
                self.passengers.remove(other)
                if len(self.passengers) == self.capacity:
                    self.has_empty_seats = False
                else:
                    self.has_empty_seats = True


bus1 = Bus(23, 4, 35, ["peter", "oleg"], {1: "peter", 2: "oleg"})
bus1.landing_or_disembarkation(["ana"], "landing")
bus1.speed_boost_or_decline(23, "Decline")
bus1 += ["maxim", "sana"]
# bus1 -= "maxim"
