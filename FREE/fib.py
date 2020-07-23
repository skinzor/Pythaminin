from functools import lru_cache
from time import time


@lru_cache(maxsize = 1200)
def fib(n):
    if n == 1 or n == 2: return 1
    else:
        return fib(n - 1) + fib(n - 1)


# starting time
start = time()

for n in range(1, 1000):
    print(f"val: {fib(n)} [ Ratio: {fib(n + 1) / fib(n)} ]") # Ratio between consecutive terms

# end time
end = time()

print(f"Runtime of the program is {end - start}")
