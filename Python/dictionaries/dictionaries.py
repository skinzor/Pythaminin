## DICTIONARIES ##
numbers = {'one': 1, 'two': 2, 'three': 3}
print(numbers)
print(numbers.get('three'))
print(numbers.get('four')) # as it isnt in dictionary it will return None
print(numbers.get('four', 'four')) # if its not present print a default value instead which is four

## to add, remove, access ##
numbers['four'] = 4
print(numbers)
# NOTE: can't have duplicate keys/values. adding them again will overwrite them

colors = {'r': 'red', 'w': 'white'}
colors.update(numbers) # TO ADD  #
print(colors)
print(colors.keys()) # prints all keys
print(colors.values()) # prints all values
print(colors.items()) # prints the list of tuples
