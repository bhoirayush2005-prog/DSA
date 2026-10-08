n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

# Remove duplicates and sort the array
arr = list(set(arr))
arr.sort()

print("Smallest element:", arr[0])
print("Second smallest element:", arr[1])
print("Second largest element:", arr[-2])
print("Largest element:", arr[-1])