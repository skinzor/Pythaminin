numbers = 200, 100, 100, 400, 200, 1000, 200, 10001

count = 0

for number in numbers:
    if number == 10001:
        break
    count += 1

print(f"Found in {count + 1} counts!")
