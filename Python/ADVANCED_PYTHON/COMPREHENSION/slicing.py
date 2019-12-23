# SLICING #

just_random = "Hello World!"
print(just_random[0])
print(just_random[-1])
print(just_random[0:5])
print(just_random[:5]) # 0 is optional
print(just_random[6:12])
print(just_random[-10:-6])

names = ['Tony', 'Uniminin', 'Nina', 'Vaxei']
print(names[0])
print(names[2])
print(names[:2])
print(names[-1])


new_names = names[:] # copy
new_names.append('Rotoxi')
print(new_names)
#################

my_list = list(range(10))
print(my_list[::2]) # 2 steps/skip
print(my_list[::-1]) # backward
print(my_list[1:6:2])

