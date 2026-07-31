import turtle

t = turtle.Turtle()
t.speed(10)
t.color("green" , "yellow")
t.shape("turtle")

screen = turtle.Screen()
screen.bgcolor("black")
t.hideturtle() 

for i in range(36):
    t.forward(100)
    t.right(170)

   
t.up(50)

for j in range(20):
    t.forward(10)
    t.right(18)

turtle.done()
