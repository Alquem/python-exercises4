#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math
def century(year):
  if year % 10 >= 1:
	  return int(year / 100) + 1
  else:
	  return int(year / 100)



#Invoke the function with any given year. 
print(century(22000))