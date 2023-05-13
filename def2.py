def login():
    usernameinput = input("Username:")
    passwordinput = input("Password:")
    if (usernameinput == "admin" and passwordinput == "567"):
        return True
    else:
        return False
def showMenu():
    print("Done!")
    print("------Shop------")
    print("1. Vat calculator")
    print("2. Price Calculator")
def MennuSelected():
    userSelected = int(input(">>>"))
def vatCalculate(price):
    vat = 7
    result = (price*vat/100)+price
    print(result)
    return result
def priceCalculate():
    one = int(input("Product One:"))
    two = int(input("Product two:"))
    return vatCalculate(one+two)

print(priceCalculate())



    
    
    
