#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  return [sum(int(n) for n in str(num))][0]


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))