number=int(input("Enter your number: "))
digits=len(str(number))
result=0
temp=number
while temp>0:
    digit=temp%10
    result+=digit**digits
    temp=temp//10
if number==result:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstropng number")