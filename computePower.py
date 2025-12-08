def compute_power(x,y):
    result=1
    while y>0:
        if y%2==0:
            x=x*x
            y>>=1
        else:
            result=result*x
            y=y-1
    return result
y=int(input("Enter your number: "))
x=int(input("Enter your number:"))
print(compute_power(x,y))