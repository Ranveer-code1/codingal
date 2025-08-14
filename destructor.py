class student:
    def __init__(self):
        print("constructor made")
    def __del__(self):
        print("destructor destoyed")
obj=student()
print(obj)

class student:
    def __init__(self):
        print("constructor made")
    def __del__(self):
        print("destructor destoyed")
obj=student()
del obj
print(obj)