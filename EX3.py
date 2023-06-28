n=int(input("enter the value : "))
for i in range(n):
    print(" "*i,end="")
    for s in range(n-i):
        print("* ",end="")
    print()
for a in range(n):
    print(" "*(n-a-1),end="")
    for j in range(a+1):
        print("* ",end="")
    print()

