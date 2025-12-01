def oddOne(a):
    res=0
    for i in a:
        res=res^i
    return res
a=[25,25,3,1,1,3,523]
print(oddOne(a))