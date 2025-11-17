a=int(input("Enter your number: "))
def countBit(a):
    count=0
    while(a):
        count+=1
        a>>=1
    print(count)
countBit(a)