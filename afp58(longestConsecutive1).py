num=input("Enter your binary number")
count=0
maxCount=0
for i in num:
    if i=="1":
        count+=1
        if count>maxCount:
            maxCount=count
    else:
        count=0
print("The longest consecutive 1 is", maxCount)