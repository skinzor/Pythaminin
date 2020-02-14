class Sample(object):
    pass


X = Sample()

print(type(X))


class Dog(object):

    # Class Object Attribute
    species = 'mammal'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


ton = Dog(breed='Huskie', name='tonny')
print("Name: {}\nSpecies: {}\nSpecies: {}".format(ton.name, ton.breed, ton.species))
