## LOOP AND CONTROL FLOW ##

# FOR LOOP LIST#
names = ['Vaxei', 'Tony', 'Uniminin']
for name in names:
    print(name)

quote = ("this is a test quote ok lol")
for chars in quote:   # this is how every it gets
    print(chars)

for numbers in range(5): # 5, starts from 0
    print(numbers)

for numbers in range(1, 5): # starting from 1 to 5, 1 less
    print(numbers)

for numbers in range(1, 10, 2): # takes 3 arguments. last 2 defines to skep 2(twice) at every it gets. 2 = 1 skip
    print(numbers)

# loop over dictionaries #
user_info = {'tony': '16', 'uniminin': '20'}
for name, age in user_info.items(): # used items
    print(f'User:{name} is {age} years old!')

names = {'red', 'green', 'blue'}
for index, name in enumerate(names): #enumerate
    print(f'Index:{index}  {name}')

## LOOP FLOW ##

if 1 > 0:
    print('ok')

if 1 == 1:
    print("yes")

b = [1, 2]
if b:
    print("OK")
c = []
if c:
    print('no') # wont print as c= none

d = False
if d:
    print("this wont run as its false")
else:
    print('will run if set to false')

# loop with if, elif, else

a = True
b = False

if a is True:
    print('ok')
elif a is False:  #elif = else if, can be used to create unlimited if's
    print("not ok")
else:
    print('B')

## CONTROLLING LOOP ##

number = 0

for numbers in range(1, 100+1):
    print(numbers)
    number += 1
    if number == 18:
        break

name = ['tony', 'nina', 'setif', 'rasd', 'oficia']
z = 0
for names in name:
    print(names)
    z += 1
    if z == 3:
        break

for names in name:
    print("User:", names)
    if names == 'rasd':
        break

colors = ['red', 'green', 'blue', 'white', 'black', 'magenta', 'orange', 'yellow']

for color in colors:
    if len(color) != 4:
        continue

    print(f'Color:{color}')
    if color == 'orange':
        break
print('Done')

num = 0
while True:
    print("Ok!")
    num += 1
    if num == 3:
        break
        
def special_id(id):
    for ids in id:
        print(ids)
    if '69' in id:
        return('Found the special ID: 69')

id = ('1', '2', '3', '4', '69')
print(special_id(id))
