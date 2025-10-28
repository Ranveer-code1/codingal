a=int(input("enter number"))
b=int(input("enter number"))

c=[]
d=[]

for i in range(1,a+1):
    if a%i==0:
        c.append(i)

for i in range(1,b+1):
    if b%i==0:
        d.append(i)

c=set(c)
d=set(d)

print(a*b/max(c.intersection(d)))