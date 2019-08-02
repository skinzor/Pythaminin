# Import Master Time
from datetime import datetime
import time
date_of_birth = input("Enter your date of birth, Ex. dd/mm/yyyy format: ")
date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
# End
print("Here are your Age statistics...")
print ("Years   : %d" % ((datetime.today() - date_of_birth).days/365))
print ("Months  : %d" % ((datetime.today() - date_of_birth).days/30))
print ("Hours   : %d" % ((datetime.today() - date_of_birth).days*24))
print ("Minutes : %d" % ((datetime.today() - date_of_birth).days*1440))
print ("Seconds : %d" % ((datetime.today() - date_of_birth).days*86400))
# End of printing>>>
