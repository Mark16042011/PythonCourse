class Rectangle:
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return self.width * 2 + self.length * 2


rectangle1 = Rectangle(5,5)
rectangle2 = Rectangle(6,6)


print(rectangle2.perimeter())




