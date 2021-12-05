# Your code here
def factorial(number):
    total = 1
    for i in range(number,0,-1):
        total *= i
    return total

print(factorial(int(input("factorial of: "))))