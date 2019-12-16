### Tuples ###

a = ()
print(type(a))
b = (1)
c = (2, )
print(type(b))
print(type(c))

### cannot use .remove, append and other stuffs like lists in tuples.
### Handy if not willing to change data/keep data safe. data wont be changed

# Tuple Formatting
user = ('Uniminin', '16', 'Iceland', 'girl')
name, age, country, gender = user
print(age)

## func + tuple ##

def http_status():
    return 200, "OK!"

code, status = http_status()

print(status)
