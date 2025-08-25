class area:
    def cal_main(self):
        pass
class square(area):
    def cal(self):
        print(" Square=L*W")
class rectangle(area):
   def cal(self):
        print("Rectangle=L*W")
class triangle(area):
    def cal(self):
        print("Triangle=H*L/2")
obj1=square()
obj1.cal()
obj2=rectangle()
obj2.cal()
obj3=triangle()
obj3.cal()