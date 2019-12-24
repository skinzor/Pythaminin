### CLASS ###
class Car:
    runs = False
    number_of_wheels = 4

    def __init__(self, name):
        print('New Car!')
        self.name = name

    def __str__(self):
        return f"My Car, The {self.name} Currently {self.runs}"
    def __repr__(self):
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f'{self.name} Car is Started!!!')
        else:
            print(f"{self.name} Car is Broken :(")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels
