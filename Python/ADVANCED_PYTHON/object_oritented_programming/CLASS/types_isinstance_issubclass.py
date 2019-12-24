### TYPES ###
print(isinstance(43, int))
print(type(43))
print(type('asds'))
print(isinstance('yes', str))
print(isinstance('asd', int))

### booleans are subclass of int
print(isinstance(True, int))

###
# Don't do this in production code, it's pretty bad!!!
print(True + True)
print(True + True + True + 1 + True + True * 5)


###
print({0, 1, False, True})
print({0, 1, True, False})
print({0, 1, True, True})
print({0, 1, False, False})

###
print(any([5235, 5235, 325]))
print(any([True, True, False]))
print(all([True, True, False]))

### they're all objects
print(issubclass(str, object))
print(issubclass(int, object))
