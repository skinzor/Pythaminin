## LIST OPERATIONS ##

numbers = 1, 2, 3, 5, 2
print(sum(numbers))
print(min(numbers)) # minimum number in variable
print(max(numbers)) # max number in variable
print(sorted(numbers)) # sorted order
print(sorted(numbers, reverse=False)) # condition

squares = [num * num for num in range(10)]
print(sum(squares))
print(min(squares))

####################
lottry_numbers_string = "3, 235, 23, 232"
lottery_nums = lottry_numbers_string
lottery_nums.split(", ")
print([int(num) for num in lottery_nums.split(", ")])
print(max([int(num) for num in lottery_nums.split(", ")]))

