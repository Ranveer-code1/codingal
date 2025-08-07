import random

b=random.randint(1,10)
a=int(input("Enter you guess here :"))

if a==b:
    print("correct")
else:
    print("Wrong. Good try. The number was", b)
