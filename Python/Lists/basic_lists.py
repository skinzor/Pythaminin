a = [] #<== empty list

print(type([]))
print(type(a))

# build in functions
name = "Uniminin"
print(name.lower())
print(name.upper())
print(len(name))

# Index
list = ['a', 'b', 'c']
# Index  0    1    2  .  Starts with 0 in python

print(list[2])  # c


#### short exercise ####
fruits = [
    'Mango',
    'Apple',
    'Orange'
]
print(fruits)
choice = int(input("Which one you want to buy? "))
print(('Purchased:', fruits[choice-1]))
