class Passport:
    def __init__(self, first_name: str, last_name: str, country: str, date_of_birth: float, numb_of_passport: int):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_of_birth = date_of_birth
        self.numb_of_passport = numb_of_passport

    def print_info(self):
        print(self.first_name, "\n" + self.last_name, "\n" + self.country, "\n" + f"{self.date_of_birth}", "\n" +
              f"{self.numb_of_passport}")


class ForeignPassport(Passport):
    def __init__(self, first_name: str, last_name: str, country: str, date_of_birth: float, numb_of_passport: int,
                 visa: str):
        super().__init__(first_name, last_name, country, date_of_birth, numb_of_passport)
        self.visa = visa

    def print_info(self):
        super().print_info()
        print("\n" + self.visa)


passport1 = Passport("vasy",'vasiliy','russia',13.0409,1)
passport2 = ForeignPassport('vany', 'ivan', 'russia', 23.0711, 2, "usbecistan")
PassportList = [passport2,passport1]
for item in PassportList:
    item.print_info()