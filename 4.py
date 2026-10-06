n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

search = int(input("Enter number to search: "))

found = False

for i in range(n):
    if arr[i] == search:
        print("Number is present at position:", i + 1)
        found = True
        break

if found == False:
    print("Number is not present in the array")