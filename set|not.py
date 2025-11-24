def setnot(number,n):
    if number&(1<<(n-1)):
        print("SET BIT")
    else:
        print("NOTSET BIT")

number=int(input("Enter Your Number: "))
n=int(input("Enter Your Bit: "))
setnot(number,n)