## ADVANCED DATA TYPE ##
knowledge = ("In order to obtain ultimate knowledge and serenity!")
print(knowledge[1]) #prints the char of place 1, python starts from 0 to x
print(knowledge[0:4]) # prints 0:4 as first to upto 4th, | 0, 1, 2 ,3 , 4 >>
print(knowledge[-1]) # negative as from last

knowledge = ['k', 'n', 'o', 'w']
print(knowledge[1]) # prints the 1st term
print(knowledge[1:3]) # from from 1th to the 3rd term
# can use negative to print from backward

knowledge.remove('k') # removes k, only first instance, duplicates are ignored
print(knowledge)
knowledge.insert(2, 'x') # insert x in 2nd place
del knowledge[0] # to delete item at 0th place

# to see if particular value,key in list
's' in knowledge # returns boolean

type({}) #empty set is a dictionary
