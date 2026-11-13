import turtle
t = turtle.Turtle()
sleep = 2.2
canvas = t.getscreen()

canvas.bgcolor("black")
t.pensize(3)
t.speed(1)
t.color("yellow")
t.begin_fill()
t.left(140)
t.forward(113)
t.circle(-57, 200)
t.left(120)
t.circle(-57, 200)
t.forward(113)
t.end_fill()
t.done()