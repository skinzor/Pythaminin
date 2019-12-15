#####       Simple 2 Number Calculator By Uniminin        ####
#### PERMISSION IS HEREBY GRANTED TO ANY COPYRIGHT HOLDER ####

print(" S I M P L E  C A L C U L A T O R  M5 ")

while True:
    def calculator(x, y, operator):
        if operator == "+":
            return x + y
        if operator == "-":
            return x - y
        if operator == "*":
            return x * y
        if operator == "/":
            return x / y

    try:
        calculate = calculator(x=int(input("Enter First Number: ")), y=int(input("Enter Second Number: ")),
                               operator=input("Operator: "))
        if calculate is None:
            print("Please Enter A Valid Operator!")
        else:
            print(calculate)

    except ValueError:
        print("Please Enter a Valid Number!")

