def OnSquareTime(n):
    iterations=0
    for i in range(0,n):
        for j in range(0,n):
            iterations+=1
            print("*",end=" ")
        print("")
    print("When 'n' is",n,",the number of iterations is",iterations)
OnSquareTime(10)
OnSquareTime(20)
OnSquareTime(30)