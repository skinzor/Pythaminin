## Conditionals ##

print(100 % 3)
print(bool(100 % 2))
print(bool(100 % 2 == 0))

even_squares = [num * num for num in range(10) if num % 2 == 0] # even squares
print(", ".join([str(even_square) for even_square in even_squares]))

my_list = [0, 1, 2, 3, 4]
my_string = ",".join([str(num) for num in my_list])
print(my_string)
