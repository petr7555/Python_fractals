import turtle
import numpy

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
window.tracer(1000)

size = 100


def spiral(size, depth):
    if depth < 0: return
    lengths = numpy.linspace(size, 0, num=5)
    for i in range(len(lengths)):
        if i == 1 or i == 2:
            position = turtle.pos()
            turtle.left(180)
            spiral(size / 2, depth - 1)
            turtle.penup()
            turtle.goto(position)
            turtle.pendown()
            turtle.left(180)
        turtle.circle(lengths[i], 180 * i)


spiral(size, 7)

window.update()
turtle.getscreen().getcanvas().postscript(file='ps_files/spiral_flat.ps')
window.exitonclick()
