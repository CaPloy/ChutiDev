number = int(input())
for x in range(number):
    print(" "*(number-(x+1)) + "*"*((x*2)+1))
    