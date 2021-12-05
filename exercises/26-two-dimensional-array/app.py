array_dimensions = input("the array dimensions are: ")
arr = []

for i in range(int(array_dimensions.split(",")[0])):
    row = []
    for j in range(int(array_dimensions.split(",")[1])):
        row.append(i*j)
    arr.append(row)

print(arr)
