from car import Car

tesla = Car('Tesla')
Car.get_number_of_wheels()
print(tesla.get_number_of_wheels())
tesla.start()

print(str(tesla))
print(repr(tesla))

import vehicle
four_by_four = vehicle.Vehicle('zoom', 'fast', fuel='oil')
my_tesla = vehicle.Car('Tesla', 'x99', fuel='diessel')
print(my_tesla.make)
print(my_tesla.model)
print(my_tesla.fuel)
print(my_tesla.num_wheels)
print(my_tesla.is_eco_friendly())
