import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
  
 # More info :
 # https://www.w3schools.com/python/python_regex.asp
 # https://regexr.com
 # https://regex101.com (Best)