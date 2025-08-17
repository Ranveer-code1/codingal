print("Use the + sign for addition")
print("Use the - sign for subtraction")
print("Use the * sign for multiplication")
print("Use the % sign for remainders")
print("Use the / sign for division")

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = input("Enter your operation: ")

if c == "*":
    print("Result:", a * b)
elif c == "%":
    print("Result:", a % b)
elif c == "-":
    print("Result:", a - b)
elif c == "+":
    print("Result:", a + b)
elif c == "/":
   
        print("Result:", a / b)
    
       
else:
    print("Invalid operation.")
