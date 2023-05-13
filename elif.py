usernameinput = input("Username:")
passwordinput = input("Password:")
if (usernameinput == "admin" and passwordinput == "567"):
    print("Done!")
    print("------Shop------")
    print("1. Vat calculator")
    print("2. Price Calculator")
    userSeclected = int(input(">>"))
    if userSeclected == 1:
        price = int(input("Price(THB)"))
        vat = 7
        result = (price*7/100)+price
        print(result)
    elif userSeclected == 2:
        one = int(input("Produc One:"))
        two = int(input("Produc One:"))
        print(one+two)
else:
    print("UserName Erro")
    print("Please Sigin Again")

