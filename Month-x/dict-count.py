counts = dict()

names = ["tony", "test", "tony", "test", "tony", "rhino", "tony", "rhino"]

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

print(counts)
