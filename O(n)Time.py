def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("The value of 'n' is",n)
    print("The number of iterations is",iteration)
OnTime(10)
OnTime(20)
OnTime(42)
print("The number of iterations depends on the value of 'n'")