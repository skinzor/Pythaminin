### PRACTICE ###

def calculator(x, y, operator):
    if operator == "+" or operator == "add":
        return x + y
    if operator == "-" or operator == "subtract":
        return x - y
    if operator == "*" or operator == "multiply":
        return x * y
    if operator == "/" or operator == "divide":
        return x / y
    
calculate = calculator(x=int(input("Enter First Number: ")), y=int(input("Enter Second Number: ")), operator=input("Operator: "))
print(calculate)
