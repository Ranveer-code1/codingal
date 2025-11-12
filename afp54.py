lower=10
higher=99
for num in range(lower,higher+1):
    

    if num>1:
        for i in range(2,num):
            if num%i==0:
               
                break
        else:
            print(num)
    