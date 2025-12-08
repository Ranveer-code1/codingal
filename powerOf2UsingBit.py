ans=0
bit=0
a=int(input("Enter your number: "))
while ans<a:
    ans=1<<bit
    if ans==a:
        print("The number is a power of 2")
        break
    bit+=1
else:
    print("The number is not a power of 2")
    