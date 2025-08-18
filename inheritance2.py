class person:
    def __init__(self,name,position):
        self.name=name
        self.pos=position
    def display(self):
        print(self.name)
        print(self.pos)
class penguin(person):
    def __init__(self,name,position,salary):
        self.sale=salary
        super().__init__(name,position)
obj=penguin("Ryan","COO","$22,345,341,4589")
obj.display()
print(obj.sale)