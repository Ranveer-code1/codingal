a=input("name of polygon :")
if a=="SQUARE""RECTANGLE""PARALLELOGRAM":
    b=int(input("Enter the height :"))
    c=int(input("Enter the length :"))
    print(b*c)
elif a=="Triangle":
    d=int(input("Enter the height :"))
    e=int(input("Enter the base :"))
    print(d*e/2)
else:
    print("Please enter a valid REGULAR POLLYGON IN THE CORRECT SPELLING AND CAPITAL LETTERS.")