class computer:
    def __init__(self):
        self.__maxprice=5800
    def display(self):
        print(self.__maxprice)
    def change(self,new):
        self.__maxprice=new
obj=computer()
obj.display()
obj.__maxprice=4700
obj.display()
obj.change(4700)
obj.display()