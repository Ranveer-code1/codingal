def setnot(number, n):
    # Check if the nth bit is set
    if number & (1 << (n - 1)):
        print("SET BIT")
    else:
        print("NOT SET BIT")

def rightmost(number):
    # Find position of rightmost set bit (1-based index)
    if number == 0:
        return None
    position = 1
    while number & 1 == 0:
        number >>= 1
        position += 1
    return position

# Example usage
number = int(input("Enter Your Number: "))
n = rightmost(number)
if n:
    setnot(number, n)
else:
    print("No set bits found")
