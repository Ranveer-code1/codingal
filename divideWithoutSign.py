def divide(dividend,divisor):
    count=0
    if divisor==0:
        print("division is not possible because the number is xero")

    while dividend >= divisor:
        dividend=dividend-divisor
        count+=1
    print(count)
divide(5,2)