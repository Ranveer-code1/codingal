def Odd2(arr,size):
    xor2=arr[0]
    for i in range(1,size):
        xor2=xor2^arr[i]
    x=0
    y=0
    setBit=0
    setBit=xor2&~(xor2-1)
    for i in range(size):
        if arr[i]&setBit:
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("The 2 odd occuring numbers are,",x, y)
arr=[45,56,1,1,2,2]
Odd2(arr,len(arr))