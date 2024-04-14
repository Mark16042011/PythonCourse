class TriangleChecker:
    def __init__(self, sides: list[int]):
        self.sides = sorted(sides)

    def is_triangle(self):
        if self.sides[0] < 0:
            print("С отрицательными числами ничего не выйдет!")
        elif self.sides[0] + self.sides[1] > self.sides[2]:
            print("Ура, можно построить треугольник!")
        else:
            print("Жаль, но из этого треугольник не сделать.")


a1 = TriangleChecker([5, 5, 1])
a1.is_triangle()