#n=int(input("enter no of rows:"))
# for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(j,end="")
#    print()


n=int(input("enter no of rows:"))
for i in range(0,1,-1):
    for j in range(0,i+1):
        print("*",end="")
    print()