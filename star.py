import turtle
turtle.Screen().bgcolor("darkred")
screen=turtle.Screen()
turtle.title("Square-1")
a=turtle.Turtle()
for i in range(3):
    a.forward(100)
    a.left(120)
a.left(90)
a.penup()
a.forward(50)
a.right(90)
a.pendown()
for i in range(3):
    a.forward(100)
    a.right(120)

turtle.done()