def integral(number):
    return {k:v*v for k,v in enumerate(range(1,number+1), start=1)}

integral_numb = int(input("insert integer number: "))
print(integral(integral_numb))