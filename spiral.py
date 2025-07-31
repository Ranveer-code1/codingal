import turtle
screen=turtle.Screen()
a=turtle.Turtle()
colors=["red","blue","green","yellow"]
a.speed(100)
for i in range(100):
    a.pencolor(colors[i%len(colors)])
    a.forward(i*5)
    a.left(100)
turtle.done()