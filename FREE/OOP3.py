class Animal(object):

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def whoAmI(self):
        print("DOG")

    def bark(self):
        print("WOOF")

dog = Dog()
dog.whoAmI()
