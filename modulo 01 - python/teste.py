import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Spain", txt)
print(type(x))
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")