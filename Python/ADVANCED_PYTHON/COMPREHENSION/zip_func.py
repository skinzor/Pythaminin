### ZIP FUNCTION ###

squares = {num: num * num for num in range(11)}
print(squares.keys())
print(squares.items())
print(squares.values())

###

names = ['Tony', 'Uniminin', 'Krey']
ages = ['16', '16', '20']
for item in zip(names, ages):
    print(item)

for name, age in zip(names, ages):
    print(f'{name} is {age} years old!')

print([f"{name} is {age} years old"for name, age in zip(names, ages)])

string = ['a', 'z']
integers = [1, 69]
print(list(zip(string, integers)))
print(dict(zip(string, integers)))
