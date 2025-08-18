class person :
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)
class penguin(person):
    def __init__(self,name,id,salary,company):
        self.salary=salary
        self.company=company
        person.__init__(self,name,id)
obj=penguin("Ron",589,"$22,345,467,443","CDS")
obj.display()
print(obj.salary)
print(obj.company)