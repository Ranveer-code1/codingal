var=int(input("Enter a number"))
if var>=50:
    print("number is over 50")
    if var%2==0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is below 50")