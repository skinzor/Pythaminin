numbers = 1, 2, 3, 5, 7, 1, 2, 10, 100, 242, 24, 856, 234, 976

last_number = 0

for number in numbers:
    number = number + last_number
    last_number = number

print(number)
