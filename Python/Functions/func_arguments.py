#### FUNC ARGUMENT

def greeting(greet, name="tony"): # default name=tony
    print(f'{name}, {greet}')

greeting("sup")
greeting("sup", "uniminin") # gets change.

def price(onion="$2", tomato="$1", mango="$4"):
    return (f'''Prices are:
Onion:{onion}
Tomato:{tomato}
Mango:{mango}''')

print(price())

print(price(onion="$5")) # value change, explicit label
