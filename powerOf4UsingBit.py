a=int(input("Enter your number: "))
if a&(a-1)==0:
    if a==1:
        print("the number is a power of 4")
        exit()
    elif a%10==4 or a%10==6:
        print("the number is a power of 4")
    else:
        print("The number is not a power of 4")
else:
    print("The number is not a power of 4")
