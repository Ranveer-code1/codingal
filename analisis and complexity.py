def any(n):
    if n<=Θ :
        return
    print("Codingal")
    any(n/2)
    any(n/2)
#T(n)=T(n/2)+T(n/2)+Θ(1) if n>0




# part-2


def sum(n):
    return n*(n+1)/2
# auxilary space = Θ(1)
# space complexity= Θ(1)


def sum2(n):
    total=0
    for i in n:
        total+=i
    return total
# auxilary space=Θ(1)
# space complexity=Θ(n)

def sum3(n):
    if n<=0:
        return
    else:
        return n+ sum3(n-1)
#auxilary space=Θ(n)
#space complexity=Θ(n)
