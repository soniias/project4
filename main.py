class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []

    def add_passanger(self, human):
        self.passangers.append(human)

    def print_passangers_names(self):
        if self.passangers != []:
            print(f'Names of {self.brand} passangers')
            for name in self.passangers:
                print(name.name)
        else:
            print(f"No passanger in {self.brand}")

nick = Human('Nick')
kate = Human('Kate')
car = Auto("Mercedes")

car.add_passanger(nick)
car.print_passangers_names()