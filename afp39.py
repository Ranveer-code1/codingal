a=int(input("enter one digit"))
b=int(input("enter one digit"))
c=int(input("enter one digit"))
d=a**3+b**3+c**3
e=int(input("enter the combined digits"))
print(d)
if d==e:
    print("Armstrong")
else:
    print("Not armstrong")