class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is",self.name,". I am",self.age,"years old.")
    def sound(self):
        print("I make the sound miaw")
class dog:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def info(self):
         print("My name is",self.name,". I am",self.age,"years old.")
    def sound(self):
        print("I make the sound bark")
dog1=dog(4,"Ron")
cat1=cat("Ryan",5)
for i in (dog1,cat1):
    i.sound()
    i.info()