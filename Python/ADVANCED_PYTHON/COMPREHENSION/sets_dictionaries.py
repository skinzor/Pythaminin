## SETS & Dictionaries ##

# 4 different "container" datatypes = lists, tuples, sets, dictionaries
print({num * num for num in range(10)}) # not ordered
print([num * num for num in range(10)]) # ordered

print({num: num * num for num in range(10)}) # set to dic
