n=int(input("Enter number of rows"))
b=int(input("Enter 1 or 0"))
b=bool(b)
for i in range(n):
    for j in range(n):
        if j<=i and b:
            print("*",end="")
        elif j<=n-1-i and not(b):
            print("*",end="")
        else:
            print("",end="")
    print("")

"""
****  0       
***   1
**    2
*     3

"""