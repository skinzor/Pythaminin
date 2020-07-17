numbers = 200, 100, 100, 400

last_number = 0
count = 0

for number in numbers:
    number = number + last_number
    last_number = number
    count += 1

print(number / count)
