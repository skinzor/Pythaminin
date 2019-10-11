# Importing Master
import random
import string
# Import Done
def randomStringwithDigitsAndSymbols(stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))
# Done fi
print ("Password Generated For you ", randomStringwithDigitsAndSymbols() )
# fi done
