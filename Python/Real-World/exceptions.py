# this will throw an error
try:
    int('abc')
except ValueError:
    print("Oopsie, you can't do that!")

print("this is the end of the program")

# Error with more details
try:
    int('abc')
except ValueError as error:
    print("oopsie. ", error)

print("this is the end of the program")
