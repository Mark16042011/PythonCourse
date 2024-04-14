class Soda:
    def __init__(self, dobavka: str = None):
        self.dobavka = dobavka

    def show_my_drink(self):
        if self.dobavka:
            print("Газировка и " + self.dobavka)
        else:
            print("Обычная газировка")


Pepsi = Soda()
Pepsi.show_my_drink()