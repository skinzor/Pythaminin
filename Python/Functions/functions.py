# Basic Functions

def name():
    name = "kotoxrii"
    print(name)

name()  # calling func with ()
print(name()) # print it with type.

def age():
    age = "20"
    return age   # returns directly

age = age()
print(age) # direct print


################################################
# 2nd level

def add_number(a, b):
    return a + b

print(add_number(input("num1 : "), input("num2 : "))) # add them as string. so a, b : 1, 2 = 12
num = add_number(3, 3)
print(num)
print(add_number(68, 1))

x = 100
y = 0
print(add_number(x, y))

def get(name):
    return "you are " + name

print(get("tony"))

def greet(greet, name):
    print(f"{greet}, {name}")
    
greet("hi","tony")
