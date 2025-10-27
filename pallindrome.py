number=int(input("Enter your number: "))

original_number=number
reverse_number=0
while number>0:
    remainder=number%10
    reverse_number=reverse_number*10+remainder
    number=number//10
if original_number==reverse_number:
    print("The number is a palindrome number.")
else:
    print("the number is not a palindrome number.")
