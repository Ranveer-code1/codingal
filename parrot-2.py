class parrot:
    def __init__(self,color):
        self.color=color
    def intro(self):
        print("My color is",self.color)

obj=parrot("blood orange")
obj.intro()