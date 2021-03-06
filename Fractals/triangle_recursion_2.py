import turtle

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
window.tracer(1000)


def triangle(a, order):
    if order > 0:
        for i in range(6):
            turtle.forward(a)
            turtle.right(60)
            triangle(a / 3, order - 1)
            turtle.left(120)
    else:
        for i in range(6):
            turtle.forward(a)
            turtle.left(60)


triangle(100, 5)
window.update()
window.update()
turtle.getscreen().getcanvas().postscript(file='ps_files/triangle_recursion_2.ps')
window.exitonclick()
