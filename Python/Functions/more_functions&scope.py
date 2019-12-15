### Empty Default Lists ###

def test(a, b=[]): # empty lists
    b.append(a) # a=b
    print("B is", b) #empty list == full
    
test(3)

##### Function Scope ########

name = "uniminin"

def name_in():
    name = "tony"
    print("Name Inside:%s" % name)

print("Name outside:%s" % name)
name_in()
