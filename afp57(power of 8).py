a=int(input("Enter your number: "))
if a&(a-1)==0:
    if a==1:
        print("the number is a power of 4")
        exit()
    elif a%8==0:
        print("the number is a power of 4")
    else:
        print("The number is not a power of 8")
else:
    print("The number is not a power of 8")
