bits=input("Enter your bit")
reverse=""
for i in range(len(bits)-1,-1,-1):
    reverse+=bits[i]
print("Original:",bits)
print("Reversed:",reverse)