def factorial(n):
    f=1
    for i in range(1,n+1):
        f=i*f
    print("The factorial of",n,"is",f,".")
n=int(input("Enter your number"))
factorial(n)