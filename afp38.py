a=int(input("enter your days: "))
b=int(input("enter your age: "))
if a-198>=-75/100:
    print("You have passed the first section of our test")
    if b<=12:
        print("You are not allowed to take the test")
    else:
        print('You are allowed to take the test')
else:
    print("You are not allowed to take the test")