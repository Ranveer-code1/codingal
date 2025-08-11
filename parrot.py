class parrot:
    pet_school="something school for something pets"
    def __init__(self,age):
        self.age=age
obj=parrot("just a number")
print("My age is",obj.age)
print("My school is called",obj.pet_school)
obj1=parrot("100")
print("My age is",obj1.age)
print("My school is called",obj1.pet_school)
