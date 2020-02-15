import sys
import time

thread = "-|-"

a = 0
for x in range (0, 3):
    a = a + 1
    b = (a * f"{thread}" + "Loading" + f"{thread}" * a)
    sys.stdout.write('\r'+b)
    time.sleep(0.5)

try:
    a.replace("3", "")
    print(a)
except AttributeError:
    pass
