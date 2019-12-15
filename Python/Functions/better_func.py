### FUNC CLEAR #####

def num(a, b=[]):
    b.append(a)
    print(b)
    
num(5)
num(7)
num(6969) # continue addition

def num2(a, b=None):
    if b is None:
        b = []
        b.append(a)
        print(b)

num2(4)     # wont be added
num2(69)
