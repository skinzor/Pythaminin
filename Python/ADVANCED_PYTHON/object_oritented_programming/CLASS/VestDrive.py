# Exercise/Practice #

class Vehicle:

    def __init__(self, name, model, owner, fuel='diesel'):
        self.name = name
        self.model = model
        self.owner = owner
        self.fuel = fuel

    def __str__(self):
        return f"{self.owner} is the owner of {self.name} {self.model} and it runs on {self.fuel}!"


info = Vehicle(input('Enter Car Name: '), input('Enter Model Number: '), input('Enter car Owner name: '))
print(info)
