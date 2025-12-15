def swap(a,b):
    print("Before swapping the values of a is",a ,"and the value of b is", b,".")
    a=a^b
    b=a^b
    a=a^b
    print("After swapping the value of a is",a,"and the value of b is",b,".")
swap(23456789862656812,235146807697860963275622)

def swap2(a,b):
    print("Before swapping the value of a is",a,"and the value of b is",b,".")
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print("After swapping the value of a is",a,"and the value of b is",b,".")
swap2(12745980,120748932671450)