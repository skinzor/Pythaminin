## LIST COMPREHENSIONS ##

names = ['tony', 'uniminin', 'nina']
print('nina'.upper())

upper_name = []
for name in names:
    upper_case_name = name.upper()
    upper_name.append(upper_case_name)
    
print(upper_name)

print([name.upper() for name in names]) # Useful, easy.
print([num * num for num in range(10)])
print([("length", len(name)) for name in names])
print(", ".join([f"Name is {name}" for name in names]))
