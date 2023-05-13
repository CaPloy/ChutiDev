correctNumber = 17
userGuesss = 0
while userGuesss!=correctNumber:
    userGuesss = int(input("Please guess a number :"))
    if userGuesss >correctNumber:
        print("Too Large")
    elif userGuesss<correctNumber:
        print("Too Small")
    elif userGuesss == correctNumber:
        print("Correct!")