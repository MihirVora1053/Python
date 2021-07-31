import random
print("You have 10 lifes in this game\n","You entered in the snake water gun game\n")
i=1
myList=["S","W","G"]
arr=[0,0]
def win():
    print("Congratulations you win")
def lose():
    print("You lose.Better luck next time")
while i<=10:
    print("Round",i)
    c=random.choice(myList)
    i=i+1
    user=input("S or W or G.Enter your choice.\n")
    if user==c:
        print("It's a tie")
        arr[0] = arr[0] + 1
        arr[1] = arr[1] + 1
    elif user=="S" and c=="W":
        win()
        arr[0] = arr[0] + 1
    elif user=="S" and c=="G":
        lose()
        arr[1] = arr[1] + 1
    elif user=="W" and c=="S":
        lose()
        arr[1] = arr[1] + 1
    elif user=="W" and c=="G":
        win()
        arr[0] = arr[0] + 1
    elif user=="G" and c=="S":
        win()
        arr[0] = arr[0] + 1
    else:
        lose()
        arr[1] = arr[1] + 1


print("User:",arr[0],"\nComputer:",arr[1])
if arr[0]==arr[1]:
    print("The game tied")
elif arr[0]>arr[1]:
    print("Congratulations you win the game YAAY!!!")
else:
    print("You lose the game :( Try Again")


