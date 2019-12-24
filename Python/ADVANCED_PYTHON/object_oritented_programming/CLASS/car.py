### CLASS ###
class Car:
    runs = False

    def start(self, name):
        self.name = name
        if self.runs:
            print(f'{self.name} Car is Started!!!')
        else:
            print(f"{self.name} Car is Broken :(")
