#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
  return int(str(num).split(".")[1][0])



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(23.567))