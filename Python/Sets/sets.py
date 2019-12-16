## SET ##

name = {'tony', 'uniminin', 'tony', 'rio', 'ktotx'}
print(name)  # repeated ones wont be printed
age = [12, 14, 14, 125, 12, 16, 11]
print(set(age)) # sets the variable stuff
# sets dont have order, cannot be indexed. / no indexing

## add, remove ##

colors = {'red', 'blue', 'green', 'black'}
print(colors)
colors.add("magenta") # adds
print(colors)
colors.discard("red") # removes
print(colors)
colors.discard("white") # dont have white in sets so it removes
print(colors)
colors.remove("green") # removes
print(colors)

# to combine with mutiple sets #
name = {'tony', 'uniminin'}
age = {'2', '12'}
name.update(age) # adds the data of those variables
print(name)
age.update('yes') # adds them as a sequence of characters
print(age)

### SET OPERATION ###
### UNION ###

colors = {'red', 'green', 'blue', 'black', 'violet', 'pink', 'white', 'yellow'}
fav_color = {'green', 'black', 'pink', 'magenta'}
colors.union(fav_color) # union = adds the sets
print(colors)
colors | fav_color # union
print(colors)

## INTERSECTION ##
fav_color & colors # intersection
print(fav_color)

## the difference ##
colors ^ fav_color # ^ <== the difference
