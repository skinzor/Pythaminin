_from_ = int(input("From: "))
_to_ = int(input("To: "))
count = 0
for number in range(_from_, _to_+2):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"There are {count} even numbers from {_from_} to {_to_}.")
