#Write a program to accept N integers into an array and calculate and display the sum of all the elements.
n = int(input("enter the number of elements:"))
arr=[]
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)
    sum = 0
for i in arr:
    sum += i
print("The sum of all elements is:", sum)