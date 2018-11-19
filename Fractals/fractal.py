import turtle

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
window.tracer(1000)


def tetragon(a, order):
    if order > 0:
        for i in [a / 3, a * (2 ** (1 / 2) / 3), a / 3, a * (2 ** (1 / 2) / 3), a / 3]:
            tetragon(i, order - 1)
            turtle.right(45)
        turtle.right(135)
    else:
        turtle.forward(a)


tetragon(250, 7)
turtle.right(180)
tetragon(250, 7)

window.update()
turtle.getscreen().getcanvas().postscript(file='ps_files/fractal.ps')
window.exitonclick()

