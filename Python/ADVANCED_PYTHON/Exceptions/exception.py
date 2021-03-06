import datetime
year = datetime.datetime.now().year

print(" B I R T H   C A L C U L A T O R !")

while True:
    def birth_calculator():
        birth_year = int(input("Enter Birth Year: "))
        age = (int(year) - birth_year)
        if birth_year >= year + 1:
            print("The birth year cannot be greater than present year!")
        elif birth_year <= 0:
            print("The birth year cannot be less than 1")
        else:
            print(f"You Are {age} years old!")
            exit()

    try:
        birth_calculator()

    except ValueError:
        print('Please Enter A Valid Number!')

    except KeyboardInterrupt:
        exit()

# Better to be specific than general, when handling errors/exception
# don't do this>
try:
    int('dont')
except Exception:
    pass
