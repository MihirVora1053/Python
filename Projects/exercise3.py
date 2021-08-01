n=88
i=5
while(i>0):
    i=i-1
    inp=int(input("Guess a number: "))
    if(inp==n):
        print("Congratulations you made it!")
        print("Number of guesses used",5-i)
        break
    else:
        if(inp<n):
            print("Try Greater")
            print("Number of guesses left",i)
            continue
        else:
            print("Try Lesser")
            print("Number of guesses left",i)
            continue
if(i==0):
    print("Game Over")

