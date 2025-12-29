def powerSet(set,setSize):
    powerSetSize=2**setSize
    inside=0
    outside=0
    for outside in range(0,powerSetSize):
        for inside in range(0,setSize):
            if ((outside&(1<<inside))>0):
                print(set[inside],end="")
        print("")
set=[1,2,3,4,5,6]
powerSet(set,len(set))