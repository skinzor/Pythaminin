## BOOLEANS ##

print(bool(0)) # 0 is always false in python
print(bool(124120))
print(bool(-1240))
print(bool([]))
print(bool({}))
print(bool(''))    # empty set, tuple, list, etc are false
print(bool(set()))
print(bool(None)) # none is false

# Comparisons
print(bool(2 == 3))
print(bool(1 > 2))
print(bool(2 != 3))

print(bool('A' < 'a')) # upper case letters are lower-valued in ASCII
print(bool('c' < 'e'))
print(bool('bat' < 'cat'))

# Variable logic
a = 1, 2
b = 1, 2
print(bool(a == b))
print(bool(a is b))

a = None
print(bool(a is None)) # is ==   | Not necessarily
print(a is not None) # not = !=

a = True
b = True
print(bool(a or b)) # either
print(bool(a and b))
print(bool(a and b is True))

b = False
print(bool(a and b)) # if any value is false then its false
print(bool(a or b)) # either true = true
print(bool(0 or 1))
print(bool([] or [2]))

not False # opposite
not True # same goes here

print(bool(False and True and True)) # returns the only first value
