def vatCalculate(totalprice):
    result = totalprice + (totalprice*7/100)
    return result
print(vatCalculate(int(input("Total Price:"))))

