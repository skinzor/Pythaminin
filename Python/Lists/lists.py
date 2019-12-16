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

### chaning order of list ###

numbers = [10, 3, 5, 1, 8, 9, 2, 4, 7, 6]
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
# actual
print(numbers)
# Sorted
print(ascending)
print(descending)

## data wont chage. to change:
numbers.sort() # changed
print(numbers)

# str
list = ['apple', 'ball', 'zend']
print(sorted(list, reverse=False))

print(dir(list)) # shows all bilt-in func about list

### Inset item in list ###

fruits = ['apple', 'orange']
more_fruit = fruits.insert(2, 'mango')
print(fruits)

vegetables = ['onion', 'tomato']

fruits.append(vegetables)
print(fruits)
vegetables.append(fruits)
print(vegetables)


## List Lookup ##
names = ['tony', 'uniminin', 'vietname', 'vietname', 'yes']
print('vietname' in names)
print('test' in names)

# 
names.index("tony") #shows the index in list
print(names.count('vietname')) # counts how many times its in the list

# to change item
names[0] = 'uniminin'
print(names)

# to remove !
games = ['avatar', 'soxz', 'osu', 'avatar']
games.remove('avatar')
print(games) # if multiple/duplicate time in lists, only first will be removed
games.pop()
print(games) # pop() <== will remove all of them

games.pop(1) # can be used to remove specific index items
