from abc import ABC
class animal(ABC):
    def move(self):
        pass
class snake(animal):
    def move(self):
        print("I can slither")
class human(animal):
    def move(self):
        print("I can drive")
class lion(animal):
    def move(self):
        print("I can walk")
obj1=snake()
obj1.move()
obj2=human()
obj2.move()
obj3=lion()
obj3.move()