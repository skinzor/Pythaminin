### CLASS ###
class Car:
    runs = False
    def __init__(self, name):
        print('New Car!')
        self.name = name

    def start(self):
        if self.runs:
            print(f'{self.name} Car is Started!!!')
        else:
            print(f"{self.name} Car is Broken :(")

