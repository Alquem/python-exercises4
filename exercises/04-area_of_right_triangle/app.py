#Complete the function to return the area of the triangle.
b = input("Size of B")
h = input("Size of H")

def area_of_triangle(arg1, arg2):
    #your code here, please remove the "None" 
    area = 0.5 * int(arg1) * int(arg2)
    return area

# Testing your function
print(area_of_triangle(b, h))