import turtle

t = turtle.Pen()
t.pendown()
t.pencolor('pink')
t.pensize(5)
t.fillcolor('yellow')
t.begin_fill()
for x in range(10):
    t.forward(5*x)
    t.left(90)
t.end_fill()
t.penup()
t.goto(10,-10)
