largestNumber=int(input("enter ur largest number"))
smallestNumber=int(input("enter ur smallest number"))
while smallestNumber:
    numberStore=smallestNumber
    smallestNumber=largestNumber%smallestNumber
    largestNumber=numberStore
print("The HCF of the numbers is",largestNumber)

