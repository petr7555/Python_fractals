import turtle

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
window.tracer(1000)


def tetragon(a, order):
    if order > 0:
        for i in [a / 3, a, a, a / 3]:
            tetragon(i, order - 1)
            turtle.right(90)
    else:
        turtle.forward(a)


tetragon(100, 5)
window.update()
turtle.getscreen().getcanvas().postscript(file='ps_files/fractal_2.ps')
window.exitonclick()
