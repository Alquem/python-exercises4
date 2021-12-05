#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    d = d * n
    c = c * n
    if c >= 100:
        d += int(c / 100)
        c -= 100 
    return d, c
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(2,34,4))
