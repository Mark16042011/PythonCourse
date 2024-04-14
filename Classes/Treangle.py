import math


class RightTriangle:
    def __init__(self, side1: float, side2: float):
        self.side1 = side1
        self.side2 = side2

    def sideChange(self, side_number: int, opiration: str, value: float):
        if side_number == 1:
            side_number = self.side1
        elif side_number == 2:
            side_number = self.side2
        if opiration == "plus":
            side_number += value
        elif opiration == "minus":
            side_number -= value
        return side_number

    def perimeter(self):
        return math.sqrt(self.side1 ** 2 + self.side2 ** 2) + self.side1 + self.side2


treangle1 = RightTriangle(4,3)
print(treangle1.perimeter())