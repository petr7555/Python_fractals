import turtle
import numpy

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
window.tracer(1000)

size = 100


def spiral(size, depth, reverse):
    if depth < 0:
        return
    lengths = numpy.geomspace(size, 1, num=20)
    for i in range(len(lengths)):
        if i == 1 or i == 2 or i == 3:
            position = turtle.pos()
            turtle.right(180)
            spiral(size / 2, depth - 1, -reverse)
            turtle.penup()
            turtle.goto(position)
            turtle.pendown()
            turtle.left(180)
        turtle.circle(lengths[i], 90 * reverse)


spiral(size, 6, 1)
window.update()
turtle.getscreen().getcanvas().postscript(file='ps_files/spiral.ps')
window.exitonclick()
